import logging 
import inspect
import os
import ssl
import typing
import warnings
import zmq

from ..param.parameterized import Parameterized, ParameterizedMetaclass 
from .constants import (LOGLEVEL, ZMQ_PROTOCOLS, HTTP_METHODS)
from .database import ThingDB, ThingInformation
from .serializers import _get_serializer_from_user_given_options, BaseSerializer, JSONSerializer
from .exceptions import BreakInnerLoop
from .action import action
from .data_classes import GUIResources, HTTPResource, RPCResource, get_organised_resources
from .utils import get_default_logger, getattr_without_descriptor_read
from .property import Property, ClassProperties
from .properties import String, ClassSelector, Selector, TypedKeyMappingsConstrainedDict
from .zmq_message_brokers import RPCServer, ServerTypes, AsyncPollingZMQServer, EventPublisher
from .state_machine import StateMachine
from .events import Event



class ThingMeta(ParameterizedMetaclass):
    """
    Metaclass for Thing, implements a ``__post_init__()`` call and instantiation of a container for properties' descriptor 
    objects. During instantiation of ``Thing``, first serializers, loggers and database connection are created, after which
    the user ``__init__`` is called. In ``__post_init__()``, that runs after user's ``__init__()``, the exposed resources 
    are segregated while accounting for any ``Event`` objects or instance specific properties created during init. Properties 
    are also loaded from database at this time. One can overload ``__post_init__()`` for any operations that rely on properties
    values loaded from database.
    """
    
    @classmethod
    def __prepare__(cls, name, bases):
        return TypedKeyMappingsConstrainedDict({},
            type_mapping = dict(
                state_machine = (StateMachine, type(None)),
                instance_name = String, 
                log_level = Selector,
                logger = ClassSelector,
                logfile = String,
                db_config_file = String,
                object_info = Property, # it should not be set by the user
            ),
            allow_unspecified_keys = True
        )

    def __new__(cls, __name, __bases, __dict : TypedKeyMappingsConstrainedDict):
        return super().__new__(cls, __name, __bases, __dict._inner)
    
    def __call__(mcls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.__post_init__()
        return instance
    
    def _create_param_container(mcs, mcs_members : dict) -> None:
        """
        creates ``ClassProperties`` instead of ``param``'s own ``Parameters`` 
        as the default container for descriptors. All properties have definitions 
        copied from ``param``.
        """
        mcs._param_container = ClassProperties(mcs, mcs_members)

    @property
    def properties(mcs) -> ClassProperties:
        """
        returns ``ClassProperties`` instance instead of ``param``'s own 
        ``Parameters`` instance. See code of ``param``.
        """
        return mcs._param_container



class Thing(Parameterized, metaclass=ThingMeta):
    """
    Subclass from here to expose python objects on the network (with HTTP/TCP) or to other processes (ZeroMQ)
    """

    __server_type__ = ServerTypes.THING
   
    # local properties
    instance_name = String(default=None, regex=r'[A-Za-z]+[A-Za-z_0-9\-\/]*', constant=True, remote=False,
                        doc="""Unique string identifier of the instance. This value is used for many operations,
                        for example - creating zmq socket address, tables in databases, and to identify the instance 
                        in the HTTP Server - (http(s)://{domain and sub domain}/{instance name}). 
                        If creating a big system, instance names are recommended to be unique.""") # type: str
    logger = ClassSelector(class_=logging.Logger, default=None, allow_None=True, remote=False, 
                        doc="""logging.Logger instance to print log messages. Default 
                            logger with a IO-stream handler and network accessible handler is created 
                            if none supplied.""") # type: logging.Logger
    rpc_serializer = ClassSelector(class_=(BaseSerializer, str), 
                        allow_None=True, default='json', remote=False,
                        doc="""Serializer used for exchanging messages with python RPC clients. Subclass the base serializer 
                        or one of the available serializers to implement your own serialization requirements; or, register 
                        type replacements. Default is JSON. Some serializers like MessagePack improve performance many times 
                        compared to JSON and can be useful for data intensive applications within python.""") # type: BaseSerializer
    json_serializer = ClassSelector(class_=(JSONSerializer, str), default=None, allow_None=True, remote=False,
                        doc="""Serializer used for exchanging messages with a HTTP clients,
                            subclass JSONSerializer to implement your own JSON serialization requirements; or, 
                            register type replacements. Other types of serializers are currently not allowed for HTTP clients.""") # type: JSONSerializer
        
    # remote paramerters
    state = String(default=None, allow_None=True, URL_path='/state', readonly=True,
                fget= lambda self : self.state_machine.current_state if hasattr(self, 'state_machine') else None,  
                doc="current state machine's state if state machine present, None indicates absence of state machine.") #type: typing.Optional[str]
    
    httpserver_resources = Property(readonly=True, URL_path='/resources/http-server', 
                        doc="object's resources exposed to HTTP client (through ``hololinked.server.HTTPServer.HTTPServer``)", 
                        fget=lambda self: self._httpserver_resources ) # type: typing.Dict[str, HTTPResource]
    rpc_resources = Property(readonly=True, URL_path='/resources/object-proxy', 
                        doc="object's resources exposed to RPC client, similar to HTTP resources but differs in details.", 
                        fget=lambda self: self._rpc_resources) # type: typing.Dict[str, RPCResource]
    gui_resources = Property(readonly=True, URL_path='/resources/portal-app', 
                        doc="""object's data read by hololinked-portal GUI client, similar to http_resources but differs 
                        in details.""",
                        fget=lambda self: GUIResources().build(self)) # type: typing.Dict[str, typing.Any]
    GUI = Property(default=None, allow_None=True, URL_path='/resources/web-gui', fget = lambda self : self._gui,
                        doc="GUI specified here will become visible at GUI tab of hololinked-portal dashboard tool")     
    object_info = Property(doc="contains information about this object like the class name, script location etc.",
                        URL_path='/object-info') # type: ThingInformation
    

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        # defines some internal fixed attributes. attributes created by us that require no validation but 
        # cannot be modified are called _internal_fixed_attributes
        obj._internal_fixed_attributes = ['_internal_fixed_attributes', 'instance_resources',
                                        '_httpserver_resources', '_rpc_resources', '_owner']        
        return obj


    def __init__(self, *, instance_name : str, logger : typing.Optional[logging.Logger] = None, 
                serializer : typing.Optional[JSONSerializer] = None, **kwargs) -> None:
        """
        Parameters
        ----------
        instance_name: str
            Unique string identifier of the instance. This value is used for many operations,
            for example - creating zmq socket address, tables in databases, and to identify the instance in the HTTP Server - 
            (http(s)://{domain and sub domain}/{instance name}). 
            If creating a big system, instance names are recommended to be unique.
        logger: logging.Logger, optional
            logging.Logger instance to print log messages. Default logger with a IO-stream handler and network 
            accessible handler is created if none supplied.
        serializer: JSONSerializer, optional
            custom JSON serializer. To use separate serializer for python RPC clients and cross-platform 
            HTTP clients, use keyword arguments rpc_serializer and json_serializer and leave this argument at None.
        **kwargs:
            rpc_serializer: BaseSerializer | str, optional 
                Serializer used for exchanging messages with python RPC clients. If string value is supplied, 
                supported are 'msgpack', 'pickle', 'serpent', 'json'. Subclass the base serializer 
                ``hololinked.server.serializer.BaseSerializer`` or one of the available serializers to implement your 
                own serialization requirements; or, register type replacements. Default is JSON. Some serializers like 
                MessagePack improve performance many times  compared to JSON and can be useful for data intensive 
                applications within python. The serializer supplied here must also be supplied to object proxy from 
                ``hololinked.client``. 
            json_serializer: JSONSerializer, optional
                serializer used for cross platform HTTP clients. 
            use_default_db: bool, Default False
                if True, default SQLite database is created where properties can be stored and loaded. There is no need to supply
                any database credentials. This value can also be set as a class attribute, see docs.
            logger_remote_access: bool, Default True
                if False, network accessible handler is not attached to the logger. This value can also be set as a 
                class attribute, see docs.
            db_config_file: str, optional
                if not using a default database, supply a JSON configuration file to create a connection. Check documentaion
                of ``hololinked.server.database``.  

        """
        if instance_name.startswith('/'):
            instance_name = instance_name[1:]
        if not isinstance(serializer, JSONSerializer) and serializer != 'json' and serializer is not None:
            raise TypeError("serializer key word argument must be JSONSerializer. If one wishes to use separate serializers " +
                            "for python clients and HTTP clients, use rpc_serializer and json_serializer keyword arguments.")
        rpc_serializer = serializer or kwargs.pop('rpc_serializer', 'json')
        json_serializer = serializer if isinstance(serializer, JSONSerializer) else kwargs.pop('json_serializer', 'json')
        rpc_serializer, json_serializer = _get_serializer_from_user_given_options(
                                                                    rpc_serializer=rpc_serializer,
                                                                    json_serializer=json_serializer
                                                                )
        super().__init__(instance_name=instance_name, logger=logger, 
                        rpc_serializer=rpc_serializer, json_serializer=json_serializer, **kwargs)

        self._prepare_logger(
                    log_level=kwargs.get('log_level', None), 
                    log_file=kwargs.get('log_file', None),
                    remote_access=kwargs.get('logger_remote_access', self.__class__.logger_remote_access if hasattr(
                                                                self.__class__, 'logger_remote_access') else False)
                )
        self._prepare_state_machine()  
        self._prepare_DB(kwargs.get('use_default_db', False), kwargs.get('db_config_file', None))   


    def __post_init__(self):
        self._owner : typing.Optional[Thing] = None 
        self._internal_fixed_attributes : typing.List[str]
        self._full_URL_path_prefix : str
        self.rpc_server : typing.Optional[RPCServer]
        self.message_broker : typing.Optional[AsyncPollingZMQServer]
        self._event_publisher : typing.Optional[EventPublisher]
        self._gui = None # filler for a future feature
        self._prepare_resources()
        self.load_properties_from_DB()
        self.logger.info(f"initialialised Thing class {self.__class__.__name__} with instance name {self.instance_name}")


    @property
    def properties(self):
        return self.parameters


    def __setattr__(self, __name: str, __value: typing.Any) -> None:
        if  __name == '_internal_fixed_attributes' or __name in self._internal_fixed_attributes: 
            # order of 'or' operation for above 'if' matters
            if not hasattr(self, __name) or getattr(self, __name, None) is None:
                # allow setting of fixed attributes once
                super().__setattr__(__name, __value)
            else:
                raise AttributeError(f"Attempted to set {__name} more than once. " +
                                     "Cannot assign a value to this variable after creation.")
        else:
            super().__setattr__(__name, __value)


    def _prepare_resources(self):
        """
        this method analyses the members of the class which have '_remote_info' variable declared
        and extracts information necessary to make RPC functionality work.
        """
        # The following dict is to be given to the HTTP server
        self._rpc_resources, self._httpserver_resources, self.instance_resources = get_organised_resources(self)


    def _prepare_logger(self, log_level : int, log_file : str, remote_access : bool = False):
        from .logger import RemoteAccessHandler
        if self.logger is None:
            self.logger = get_default_logger(self.instance_name, 
                                    logging.INFO if not log_level else log_level, 
                                    None if not log_file else log_file)
        if remote_access:
            if not any(isinstance(handler, RemoteAccessHandler) for handler in self.logger.handlers):
                self._remote_access_loghandler = RemoteAccessHandler(instance_name='logger', 
                                                    maxlen=500, emit_interval=1, logger=self.logger) 
                                                    # thing has its own logger so we dont recreate one for
                                                    # remote access handler
                self.logger.addHandler(self._remote_access_loghandler)
        
        if not isinstance(self, logging.Logger):
            for handler in self.logger.handlers:
                # if remote access is True or not, if a default handler is found make a variable for it anyway
                if isinstance(handler, RemoteAccessHandler):
                    self._remote_access_loghandler = handler        


    def _prepare_state_machine(self):
        if hasattr(self, 'state_machine'):
            self.state_machine._prepare(self)
            self.logger.debug("setup state machine")

    
    def _prepare_DB(self, default_db : bool = False, config_file : str = None):
        if not default_db and not config_file: 
            self.object_info
            return 
        # 1. create engine 
        self.db_engine = ThingDB(instance=self, config_file=None if default_db else config_file, 
                                    serializer=self.rpc_serializer) # type: ThingDB 
        # 2. create an object metadata to be used by different types of clients
        object_info = self.db_engine.fetch_own_info()
        if object_info is not None:
            self._object_info = object_info
        # 3. enter properties to DB if not already present 
        if self.object_info.class_name != self.__class__.__name__:
            raise ValueError("Fetched instance name and class name from database not matching with the ", 
                " current Thing class/subclass. You might be reusing an instance name of another subclass ", 
                "and did not remove the old data from database. Please clean the database using database tools to ", 
                "start fresh.")


    @object_info.getter
    def _get_object_info(self):
        if not hasattr(self, '_object_info'):
            self._object_info = ThingInformation(
                    instance_name  = self.instance_name, 
                    class_name     = self.__class__.__name__,
                    script         = os.path.dirname(os.path.abspath(inspect.getfile(self.__class__))),
                    http_server    = "USER_MANAGED", 
                    kwargs         = "USER_MANAGED",  
                    eventloop_instance_name = "USER_MANAGED", 
                    level          = "USER_MANAGED", 
                    level_type     = "USER_MANAGED"
                )  
        return self._object_info
    
    @object_info.setter
    def _set_object_info(self, value):
        self._object_info = ThingInformation(**value)  
      
    
    @action(URL_path='/properties', http_method=HTTP_METHODS.GET)
    def _get_properties(self, **kwargs) -> typing.Dict[str, typing.Any]:
        """
        """
        data = {}
        if len(kwargs) == 0:
            for parameter in self.properties.descriptors.keys():
                data[parameter] = self.properties[parameter].__get__(self, type(self))
        elif 'names' in kwargs:
            names = kwargs.get('names')
            if not isinstance(names, (list, tuple, str)):
                raise TypeError(f"Specify properties to be fetched as a list, tuple or comma separated names. Givent type {type(names)}")
            if isinstance(names, str):
                names = names.split(',')
            for requested_parameter in names:
                if not isinstance(requested_parameter, str):
                    raise TypeError(f"parameter name must be a string. Given type {type(requested_parameter)}")
                data[requested_parameter] = self.properties[requested_parameter].__get__(self, type(self))
        elif len(kwargs.keys()) != 0:
            for rename, requested_parameter in kwargs.items():
                data[rename] = self.properties[requested_parameter].__get__(self, type(self))                   
        return data 
    
    @action(URL_path='/properties', http_method=HTTP_METHODS.PATCH)
    def _set_properties(self, **values : typing.Dict[str, typing.Any]) -> None:
        """ 
        set properties whose name is specified by keys of a dictionary
        
        Parameters
        ----------
        values: Dict[str, Any]
            dictionary of parameter names and its values
        """
        for name, value in values.items():
            setattr(self, name, value)


    @property
    def event_publisher(self) -> EventPublisher:
        """
        event publishing PUB socket owning object, valid only after 
        ``run()`` is called, otherwise raises AttributeError.
        """
        try:
            return self._event_publisher 
        except AttributeError:
            raise AttributeError("event publisher not yet created.") from None
                
    @event_publisher.setter
    def event_publisher(self, value : EventPublisher) -> None:
        if hasattr(self, '_event_publisher'):
            raise AttributeError("Can set event publisher only once.")
        
        def recusively_set_event_publisher(obj : Thing, publisher : EventPublisher) -> None:
            for name, evt in inspect._getmembers(obj, lambda o: isinstance(o, Event), getattr_without_descriptor_read):
                assert isinstance(evt, Event), "object is not an event"
                # above is type definition
                evt.publisher = publisher 
                evt._remote_info.socket_address = publisher.socket_address
            for prop in self.properties.descriptors.values():
                if prop.observable:
                    assert isinstance(prop._observable_event, Event), "observable event logic error in event_publisher set"
                    prop._observable_event.publisher = publisher 
                    prop._observable_event._remote_info.socket_address = publisher.socket_address
            if (hasattr(obj, 'state_machine') and isinstance(obj.state_machine, StateMachine) and 
                        obj.state_machine.state_change_event is not None):                
                obj.state_machine.state_change_event.publisher = publisher 
                obj.state_machine.state_change_event._remote_info.socket_address = publisher.socket_address
            for name, obj in inspect._getmembers(obj, lambda o: isinstance(o, Thing), getattr_without_descriptor_read):
                if name == '_owner':
                    continue 
                recusively_set_event_publisher(obj, publisher)
            obj._event_publisher = publisher            

        recusively_set_event_publisher(self, value)


    @action(URL_path='/properties/db-reload', http_method=HTTP_METHODS.POST)
    def load_properties_from_DB(self):
        """
        Load and apply parameter values which have ``db_init`` or ``db_persist``
        set to ``True`` from database
        """
        if not hasattr(self, 'db_engine'):
            return
        for name, resource in inspect._getmembers(self, lambda o : isinstance(o, Thing), getattr_without_descriptor_read): 
            if name == '_owner':
                continue
        missing_properties = self.db_engine.create_missing_properties(self.__class__.properties.db_init_objects,
                                                                    get_missing_properties=True)
        # 4. read db_init and db_persist objects
        for db_param in self.db_engine.get_all_properties():
            try:
                if db_param.name not in missing_properties:
                    setattr(obj, db_param.name, db_param.value) # type: ignore
            except Exception as ex:
                self.logger.error(f"could not set attribute {db_param.name} due to error {str(ex)}")

        
    @action(URL_path='/resources/postman-collection', http_method=HTTP_METHODS.GET)
    def get_postman_collection(self, domain_prefix : str = None):
        """
        organised postman collection for this object
        """
        from .api_platform_utils import postman_collection
        return postman_collection.build(instance=self, 
                    domain_prefix=domain_prefix if domain_prefix is not None else self._object_info.http_server)
    
    @action(URL_path='/resources/wot-td', http_method=HTTP_METHODS.GET)
    def get_thing_description(self, authority : typing.Optional[str] = None): 
                            # allow_loose_schema : typing.Optional[bool] = False): 
        """
        generate thing description schema of Web of Things https://www.w3.org/TR/wot-thing-description11/.
        one can use the node-wot as a client for the object with the generated schema 
        (https://github.com/eclipse-thingweb/node-wot). Other WoT related tools based on TD will be compatible. 
        Composed Things that are not the top level object is currently not supported.
        
        Parameters
        ----------
        authority: str, optional
            protocol with DNS or protocol with hostname+port, for example 'https://my-pc:8080' or 
            'http://my-pc:9090' or 'https://IT-given-domain-name'. If absent, a value will be automatically
            given using ``socket.gethostname()`` and the port at which the last HTTPServer (``hololinked.server.HTTPServer``) 
            attached to this object was running.

        Returns:
        hololinked.wot.td.ThingDescription
            represented as an object in python, gets automatically serialized to JSON when pushed out of the socket. 
        """
        # allow_loose_schema: bool, optional, Default False 
        #     Experimental properties, actions or events for which schema was not given will be supplied with a suitable 
        #     value for node-wot to ignore validation or claim the accessed value for complaint with the schema.
        #     In other words, schema validation will always pass.  
        from .td import ThingDescription
        return ThingDescription().build(self, authority or self._object_info.http_server,
                                            allow_loose_schema=False) #allow_loose_schema)
    
    
    @action(URL_path='/exit', http_method=HTTP_METHODS.POST)                                                                                                                                          
    def exit(self) -> None:
        """
        Exit the object without killing the eventloop that runs this object. If Thing was 
        started using the run() method, the eventloop is also killed. This method can
        only be called remotely.
        """
        if self._owner is None:
            raise BreakInnerLoop
        else:
            warnings.warn("call exit on the top object, composed objects cannot exit the loop.", RuntimeWarning)
 

    def run(self, 
            zmq_protocols : typing.Union[typing.Sequence[ZMQ_PROTOCOLS], 
                                         ZMQ_PROTOCOLS] = ZMQ_PROTOCOLS.IPC, 
            # expose_eventloop : bool = False,
            **kwargs 
        ) -> None:
        """
        Quick-start ``Thing`` server by creating a default eventloop & ZMQ servers. This 
        method is blocking until exit() is called.

        Parameters
        ----------
        zmq_protocols: Sequence[ZMQ_PROTOCOLS] | ZMQ_Protocools, Default ZMQ_PROTOCOLS.IPC or "IPC"
            zmq transport layers at which the object is exposed. 
            TCP - provides network access apart from HTTP - please supply a socket address additionally.  
            IPC - inter process communication - connection can be made from other processes running 
            locally within same computer. No client on the network will be able to contact the object using
            this transport. INPROC - one main python process spawns several threads in one of which the ``Thing``
            the running. The object can be contacted by a client on another thread but neither from other processes 
            or the network. One may use more than one form of transport.  All requests made will be anyway queued internally
            irrespective of origin. 
        
        **kwargs
            tcp_socket_address: str, optional
                socket_address for TCP access, for example: tcp://0.0.0.0:61234
        """
        # expose_eventloop: bool, False
        #     expose the associated Eventloop which executes the object. This is generally useful for remotely 
        #     adding more objects to the same event loop.
        # dont specify http server as a kwarg, as the other method run_with_http_server has to be used
        
        context = zmq.asyncio.Context()
        self.rpc_server = RPCServer(
                                instance_name=self.instance_name, 
                                server_type=self.__server_type__.value, 
                                context=context, 
                                protocols=zmq_protocols, 
                                rpc_serializer=self.rpc_serializer, 
                                json_serializer=self.json_serializer, 
                                socket_address=kwargs.get('tcp_socket_address', None),
                                logger=self.logger
                            ) 
        self.message_broker = self.rpc_server.inner_inproc_server
        self.event_publisher = self.rpc_server.event_publisher 

        from .eventloop import EventLoop
        self.event_loop = EventLoop(
                    instance_name=f'{self.instance_name}/eventloop', 
                    things=[self], 
                    logger=self.logger,
                    rpc_serializer=self.rpc_serializer, 
                    json_serializer=self.json_serializer, 
                    expose=False, # expose_eventloop
                )
        
        if kwargs.get('http_server', None):
            from .HTTPServer import HTTPServer
            httpserver = kwargs.pop('http_server')
            assert isinstance(httpserver, HTTPServer)
            httpserver._zmq_protocol = ZMQ_PROTOCOLS.INPROC
            httpserver._zmq_socket_context = context
            httpserver._zmq_event_context = self.event_publisher.context
            assert httpserver.all_ok
            httpserver.tornado_instance.listen(port=httpserver.port, address=httpserver.address)
        self.event_loop.run()


    def run_with_http_server(self, port : int = 8080, address : str = '0.0.0.0', 
                # host : str = None, 
                allowed_clients : typing.Union[str, typing.Iterable[str]] = None,   
                ssl_context : ssl.SSLContext = None, # protocol_version : int = 1, 
                # network_interface : str = 'Ethernet', 
                **kwargs):
        """
        Quick-start ``Thing`` server by creating a default eventloop & servers. This 
        method is fully blocking.

        Parameters
        ----------
        port: int
            the port at which the HTTP server should be run (unique)
        address: str
            set custom IP address, default is localhost (0.0.0.0)
        ssl_context: ssl.SSLContext | None
            use it for highly customized SSL context to provide encrypted communication
        allowed_clients
            serves request and sets CORS only from these clients, other clients are rejected with 403. Unlike pure CORS
            feature, the server resource is not even executed if the client is not an allowed client.
        **kwargs,
            certfile: str
                alternative to SSL context, provide certificate file & key file to allow the server to create a SSL connection on its own
            keyfile: str
                alternative to SSL context, provide certificate file & key file to allow the server to create a SSL connection on its own
            request_handler: RPCHandler
                custom web request handler of your choice
            event_handler: BaseHandler | EventHandler
                custom event handler of your choice for handling events
        """
        # network_interface: str
        #     Currently there is no logic to detect the IP addresss (as externally visible) correctly, therefore please 
        #     send the network interface name to retrieve the IP. If a DNS server is present, you may leave this field
        # host: str
        #     Host Server to subscribe to coordinate starting sequence of things & web GUI
        
        from .HTTPServer import HTTPServer
        
        http_server = HTTPServer(
            [self.instance_name], logger=self.logger, serializer=self.json_serializer, 
            port=port, address=address, ssl_context=ssl_context,
            allowed_clients=allowed_clients,
            # network_interface=network_interface, 
            **kwargs,
        )
        
        self.run(
            zmq_protocols=ZMQ_PROTOCOLS.INPROC,
            http_server=http_server
        )

       



