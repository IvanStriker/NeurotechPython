import sys
import functools

import requests.exceptions


def trace(func=None, *, handle=sys.stdout):
    print(f"decorated func: {func}, {handle}")
    if func is None:
        print('func is None')
        return lambda func: trace(func, handle=handle)
    else:
        print(f'{func.__name__}, {handle}')

    @functools.wraps(func)
    def inner(*args, **kwargs):
        handle.write(f"Using handling output\n")
        try:
            res = func(*args, **kwargs)
            return res
        except requests.exceptions.RequestException as e:
            handle.write(f"Ошибка при запросе к API: {e}")
            raise ValueError('Упали с исключением')


    # print('return inner')
    return inner