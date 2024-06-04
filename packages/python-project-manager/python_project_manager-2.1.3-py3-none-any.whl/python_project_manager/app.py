import importlib
import re
from types import ModuleType
from typing import Callable
from python_project_manager import Config

ACTIVATE_VENV = f'venv\\Scripts\\activate'
DEACTIVATE_VENV = f'venv\\Scripts\\deactivate'

def sanitize_string_for_file(string: str) -> str:
    """
    Sanitizes a string for use as a file name by removing leading/trailing whitespace
    and replacing spaces and hyphens with underscores.

    Args:
        string (str): The string to be sanitized.

    Returns:
        str: The sanitized string.
    """
    sanitized_string = string.strip()
    sanitized_string = re.sub(r' |-', '_', sanitized_string)
    return sanitized_string

def sanitize_string_for_module(string: str) -> str:
    """
    Sanitizes a string for use as a module name.

    Args:
        string (str): The string to be sanitized.

    Returns:
        str: The sanitized string.

    """

    sanitized_string = string.strip()
    sanitized_string = re.sub(r' ', '_', sanitized_string)
    return sanitized_string

def pass_command_to_engine(_command: str, _method: Callable[..., bool], **_kwargs) -> bool:
    '''
    Passes the command to the engine if it exists, otherwise calls the method directly.

    Args:
        _command (str): The command to pass to the engine.
        _method (Callable[..., bool]): The method to call if the engine does not exist
            or if the engine needs to call the method.
        **_kwargs: The keyword arguments to pass to the method.
    '''
    try:
        # built-in engines
        engine = get_engine(_kwargs.get('_engine', Config.get('engine'))) # Get the engine if '_engine' use it, otherwise use the 'engine' from the Config

        if engine == '':
            return _method(**_kwargs)

        method: Callable[..., bool] = getattr(engine, _command, None)
        if method:
            keep_processing = method(_method, **_kwargs)
            # If keep_processing is None or True, continue processing
            if keep_processing is None or keep_processing:
                return _method(**_kwargs)
        else:
            return _method(**_kwargs)

    except Exception as e:
        raise e

def get_engine(engine_name: str) -> ModuleType | None:
    '''
    Gets the engine module by name.

    Args:
        engine_name (str): The name of the engine module to get.
    '''
    if engine_name == None or engine_name == '':
        return engine_name
    match engine_name:
        case 'ppm-builtin-setuptools': # Built-in engine
            return importlib.import_module('.builtin_engines.builtin_setuptools', package='python_project_manager')
        case 'ppm-builtin-pyinstaller': # Built-in engine
            return importlib.import_module('.builtin_engines.builtin_pyinstaller', package='python_project_manager')
        case _: # External engine
            return importlib.import_module(sanitize_string_for_file(engine_name))
