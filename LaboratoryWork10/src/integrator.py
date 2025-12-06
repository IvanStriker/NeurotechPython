from typing import Callable
from functools import partial
import concurrent.futures as futures

from my_decorators import check_types


@check_types(func=Callable, start=float|int,
             end=float|int, steps=int)
def integrate(func: Callable[[float], float],
              start: float,
              end: float,
              *,
              steps: int = 1000) -> float:
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
    res: float = 0
    step: float = (end - start) // steps
    for i in range(steps):
        res += func(start + i * step) * step
    return res
# tests + timeit


# doc + timeit + graph
@check_types(func=Callable, start=float|int,
             end=float|int, steps=int, jobs=int)
def integrateAsync(func: Callable[[float], float],
                   start: float,
                   end: float,
                   *,
                   steps: int = 1000,
                   jobs: int = 2) -> float:
    with futures.ThreadPoolExecutor(max_workers=jobs) as executor:
        threadStart = partial(executor.submit, integrate, func, steps=steps)

        step = (end - start) // jobs
        results = [threadStart(start + i * step, start + (i + 1) * step)
                   for i in range(jobs)]
        return sum([i.result() for i in futures.as_completed(results)])


# doc + timeit + graph
@check_types(func=Callable, start=float|int,
             end=float|int, steps=int, jobs=int)
def integrateProcessAsync(func: Callable[[float], float],
                          start: float,
                          end: float,
                          *,
                          steps: int = 1000,
                          jobs: int = 2) -> float:
    with futures.ProcessPoolExecutor(max_workers=jobs) as executor:
        threadStart = partial(executor.submit, integrate, func, steps=steps)

        step = (end - start) // jobs
        results = [threadStart(start + i * step, start + (i + 1) * step)
                   for i in range(jobs)]
        return sum([i.result() for i in futures.as_completed(results)])
