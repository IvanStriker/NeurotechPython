import math
import timeit
from typing import Callable

import integrator
import cintegrator

from LaboratoryWork9.src.utils.decorators import check_types


def testF(x: float) -> float:
    """
    Simple linear test function for
    benchmarking integration.

    Args:
        x (float): Input value

    Returns:
        float: x + 1
    """
    return x + 1


@check_types(Callable, str)
def printScoreFor(func: Callable, text: str):
    """
    Benchmarks an integration function and prints the result.

    Args:
        func (Callable): Integration function to benchmark
        text (str): Descriptive label for output
    """
    print(text,
          min(timeit.repeat(lambda: func(testF, 1.0, 100.0),
                            number=1000, repeat=5)))


def printScoresPartial():
    """
    Accomplishes benchmarks for all the
    six integration variants.
    """
    printScoreFor(integrator.integrate,
                  "Ordinary python:")
    printScoreFor(integrator.integrateAsync,
                  "MultyThreading python:")
    printScoreFor(integrator.integrateProcessAsync,
                  "MultyProcessing python:")
    printScoreFor(cintegrator.integrate,
                  "Ordinary cython:")
    printScoreFor(cintegrator.integrateAsync,
                  "MultyThreading cython:")
    printScoreFor(cintegrator.integrateProcessAsync,
                  "MultyProcessing cython:")


def printScore():
    """
    Entry point
    """
    printScoresPartial()


printScore()