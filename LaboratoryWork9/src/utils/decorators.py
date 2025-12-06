import sys
import functools

import requests.exceptions
import logging


def logger(func=None, *, handle=sys.stdout):
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
        success: bool = True
        try:
            res = func(*args, **kwargs)
            return res
        except requests.exceptions.RequestException as e:
            success = False
            error_amount += 1
            error(f"{error_amount}. Error: when requesting API: {e}")
            raise e
        except Exception as e:
            success = False
            error_amount += 1
            error(f"!!=>{error_amount}. Error: when requesting API: {e}")
            raise e
        finally:
            info(f"Executing of {func.__name__} finished {
                "successfully" if success else "with an error"
            }")


    # print('return inner')
    return inner