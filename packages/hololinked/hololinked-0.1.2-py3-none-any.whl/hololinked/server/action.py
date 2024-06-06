import typing
from enum import Enum
from types import FunctionType
from inspect import iscoroutinefunction, getfullargspec

from .data_classes import RemoteResourceInfoValidator
from .constants import USE_OBJECT_NAME, UNSPECIFIED, HTTP_METHODS, JSON


   
def action(URL_path : str = USE_OBJECT_NAME, http_method : str = HTTP_METHODS.POST, 
            state : typing.Optional[typing.Union[str, Enum]] = None, input_schema : typing.Optional[JSON] = None,
            output_schema : typing.Optional[JSON] = None, create_task : bool = False) -> typing.Callable:
    """
    Use this function as a decorate on your methods to make them accessible remotely. For WoT, an action affordance schema 
    for the method is generated.
    
    Parameters
    ----------
    URL_path: str, optional 
        The path of URL under which the object is accessible. defaults to name of the object.
    http_method: str, optional
        HTTP method (GET, POST, PUT etc.). defaults to POST.
    state: str | Tuple[str], optional 
        state machine state under which the object can executed. When not provided,
        the action can be executed under any state.
    input_schema: JSON 
        schema for arguments to validate them.
    output_schema : JSON 
        schema for return value, currently only used to inform clients which is supposed to validate on its won. 
        
    Returns
    -------
    Callable
        returns the callable object as it is
    """
    
    def inner(obj):
        original = obj
        if isinstance(obj, classmethod):
            obj = obj.__func__
        if obj.__name__.startswith('__'):
            raise ValueError(f"dunder objects cannot become remote : {obj.__name__}")
        if callable(obj):
            if hasattr(obj, '_remote_info') and not isinstance(obj._remote_info, RemoteResourceInfoValidator): 
                raise NameError(
                    "variable name '_remote_info' reserved for hololinked package. ",  
                    "Please do not assign this variable to any other object except hololinked.server.data_classes.RemoteResourceInfoValidator."
                )             
            else:
                obj._remote_info = RemoteResourceInfoValidator() 
            obj_name = obj.__qualname__.split('.')
            if len(obj_name) > 1: # i.e. its a bound method, used by Thing
                if URL_path == USE_OBJECT_NAME: 
                    obj._remote_info.URL_path = f'/{obj_name[1]}'
                else:
                    if not URL_path.startswith('/'):
                        raise ValueError(f"URL_path should start with '/', please add '/' before '{URL_path}'")
                    obj._remote_info.URL_path = URL_path
                obj._remote_info.obj_name = obj_name[1] 
            elif len(obj_name) == 1 and isinstance(obj, FunctionType):  # normal unbound function - used by HTTPServer instance
                if URL_path is USE_OBJECT_NAME:
                    obj._remote_info.URL_path = '/{}'.format(obj_name[0])
                else:
                    if not URL_path.startswith('/'):
                        raise ValueError(f"URL_path should start with '/', please add '/' before '{URL_path}'")
                    obj._remote_info.URL_path = URL_path
                obj._remote_info.obj_name = obj_name[0] 
            else:
                raise RuntimeError(f"Undealt option for decorating {obj} or decorators wrongly used")
            if http_method is not UNSPECIFIED:  
                if isinstance(http_method, str):
                    obj._remote_info.http_method = (http_method,)
                else:
                    obj._remote_info.http_method = http_method 
            if state is not None:
                if isinstance(state, (Enum, str)):
                    obj._remote_info.state = (state,)
                else:
                    obj._remote_info.state = state     
            if 'request' in getfullargspec(obj).kwonlyargs:
                obj._remote_info.request_as_argument = True
            obj._remote_info.isaction = True
            obj._remote_info.iscoroutine = iscoroutinefunction(obj)
            obj._remote_info.argument_schema = input_schema
            obj._remote_info.return_value_schema = output_schema
            obj._remote_info.obj = original
            return original
        else:
            raise TypeError(
                "target for action or is not a function/method. " +
                f"Given type {type(obj)}"
            )
            
    return inner 



__all__ = [
    action.__name__
]


