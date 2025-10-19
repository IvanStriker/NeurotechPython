import inspect
from typing import *
from functools import wraps


def check_types(*upper_args, **upper_kwargs):
    """
    Decorator checking all the function's arguments' types to match
    the signature. For in-class methods first argument given to this
    decorator must be Any.

    Taken from https://ru.stackoverflow.com/

    Args:
        upper_args: Types for the respective positional
            function's arguments
        upper_kwargs: Types for the respective keyword
            function's arguments

    Raises:
        TypeError: If the arguments' types doesn't match the signature
    """
    def decorate(func: Callable):
        inspector = inspect.signature(func)
        bound_types = inspector.bind_partial(
            *upper_args, **upper_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = inspector.bind(*args, **kwargs).arguments
            for name, value in bound_values.items():
                if bound_types[name] == Any:
                    continue
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            f"Argument '{name}' must be of "
                            f"'{bound_types[name]}' type."
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorate