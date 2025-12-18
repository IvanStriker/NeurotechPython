import concurrent.futures as futures
import cython
import numba

cpdef double integrate(object func,
                       double start,
                       double end,
                       int steps = 1000):
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
    cdef:
       double res = 0.0
       double step = (end - start) / steps
       int i = 0
    while i < steps:
        res += func(start + i * step)
        i += 1
    return res * step
# tests + timeit

# doc + timeit + graph
cpdef double integrateAsync(object func,
                            double start,
                            double end,
                            int steps = 1000,
                            int jobs = 2):
    """
    Calculates the definite integral of the function given.
    Uses multithreading to optimize.

    Args:
        func (Callable[[float], float]): Function to integrate
        start (float): Left edge of integration
        end (float): Right edge of integration
        steps (int): Amount of integration's segments
        jobs (int): Precise amount of threads being used

    Returns:
        float: definite integral
    """
    with futures.ThreadPoolExecutor(max_workers=jobs) as executor:
        step: cython.float = (end - start) / jobs
        results: cython.list = [executor.submit(
                                             integrate,
                                             func, start + i * step,
                                             start + (i + 1) * step,
                                             steps
                                         )
                               for i in range(jobs)]
        return sum([i.result() for i in futures.as_completed(results)])


# doc + timeit + graph
cpdef double integrateProcessAsync(object func,
                                   double start,
                                   double end,
                                   int steps = 1000,
                                   int jobs = 2):
    """
    Calculates the definite integral of the function given.
    Uses multiprocessing to optimize.

    Args:
        func (Callable[[float], float]): Function to integrate
        start (float): Left edge of integration
        end (float): Right edge of integration
        steps (int): Amount of integration's segments
        jobs (int): Precise amount of processes being used

    Returns:
        float: definite integral
    """
    with futures.ProcessPoolExecutor(max_workers=jobs) as executor:
        step: cython.float = (end - start) / jobs
        results: cython.list = [executor.submit(
                                             integrate,
                                             func, start + i * step,
                                             start + (i + 1) * step,
                                             steps
                                         )
                               for i in range(jobs)]
        return sum([i.result() for i in futures.as_completed(results)])