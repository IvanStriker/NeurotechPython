import sys
import functools
import inspect
from typing import *
from functools import wraps

import requests.exceptions
import logging


def logger(func: Callable = None, *, handle=sys.stdout):
    """
    A simple logging decorator.

    Args:
        func: Function to decorate
        handle: Stream for logging

    Returns:
        The decorated function
    """
    if isinstance(handle, logging.Logger):
        info = handle.info
        error = handle.error
    else:
        info = error = handle.write

    if func is None:
        return lambda f: logger(f, handle=handle)

    info(f"Function {func.__name__} is being traced now...")

    error_amount: int = 0

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal error_amount
        info(f"Calling {func.__name__} with params: " +
             args.__str__() +
             [[key, val] for key, val in kwargs.items()].__str__())
        info("\n")
        success: bool = True
        try:
            res = func(*args, **kwargs)
            return res
        except requests.exceptions.RequestException as e:
            success = False
            error_amount += 1
            error(f"!!=>{error_amount}. Error: when requesting API: {e}" + "\n")
            raise e
        except Exception as e:
            success = False
            error_amount += 1
            error(f"!!=>{error_amount}. Error: when requesting API: {e}" + "\n")
            raise e
        finally:
            info(f"Executing of {func.__name__} finished {
            "successfully\n" if success else "with an error\n"
            }")

    # print('return inner')
    return inner


def check_types(*upper_args, **upper_kwargs):
    """
    Decorator checking all the function's arguments' types to match
    the signature. For in-class methods first argument given to this
    decorator must be Any.

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
