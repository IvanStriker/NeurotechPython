import timeit
from typing import Callable

import integrator
import cintegrator


def printScoreFor(func: Callable[[Callable[[float], float],
                                  float, float], float],
                  text: str):
    print(text,
          min(timeit.repeat(lambda: func(lambda y: y + 1, 1.0, 100.0),
                            number=1000, repeat=5)))


def printScore():
    printScoreFor(integrator.integrate,
                  "Ordinary python:")
    printScoreFor(integrator.integrateAsync,
                  "MultyThreading python:")
    # printScoreFor(integrator.integrateProcessAsync,
    #               "MultyProcessing python:")

    printScoreFor(cintegrator.integrate,
                  "Ordinary cython:")
    printScoreFor(cintegrator.integrateAsync,
                  "MultyThreading cython:")
    # printScoreFor(cintegrator.integrateProcessAsync,
    #               "MultyProcessing cython:")