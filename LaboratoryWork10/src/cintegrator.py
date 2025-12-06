from typing import Callable
from functools import partial
import concurrent.futures as futures
import cython


def integrate(func: Callable[[cython.float], cython.float],
              start: cython.float,
              end: cython.float,
              *,
              steps: cython.int = 1000) -> cython.float:
    """
    Calculates the definite integral of the function given.

    Args:
        func (Callable[[float], float]): Function to integrate
        start (float): Left edge of integration
        end (float): Right edge of integration
        steps (int): Amount of integration's segments

    Returns:
        float: definite integral
    """
    res: cython.float = 0
    step: cython.float = (end - start) // steps
    for i in range(steps):
        res += func(start + i * step) * step
    return res
# tests + timeit

# doc + timeit + graph
def integrateAsync(func: Callable[[cython.float], cython.float],
                   start: cython.float,
                   end: cython.float,
                   *,
                   steps: cython.int = 1000,
                   jobs: cython.int = 2) -> cython.float:
    with futures.ThreadPoolExecutor(max_workers=jobs) as executor:
        threadStart = partial(executor.submit, integrate, func, steps=steps)

        step: cython.float = (end - start) // jobs
        results = [threadStart(start + i * step, start + (i + 1) * step)
                   for i in range(jobs)]
        return sum([i.result() for i in futures.as_completed(results)])


# doc + timeit + graph
def integrateProcessAsync(func: Callable[[cython.float], cython.float],
                          start: cython.float,
                          end: cython.float,
                          *,
                          steps: cython.int = 1000,
                          jobs: cython.int = 2) -> cython.float:
    with futures.ProcessPoolExecutor(max_workers=jobs) as executor:
        threadStart = partial(executor.submit, integrate, func, steps=steps)

        step = (end - start) // jobs
        results = [threadStart(start + i * step, start + (i + 1) * step)
                   for i in range(jobs)]
        return sum([i.result() for i in futures.as_completed(results)])
