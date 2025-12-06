import logging
import math
from logging.handlers import RotatingFileHandler

from decorators import loggerSolveQuadratics, WarningError

log = logging.getLogger("fileLogger")
handler = RotatingFileHandler("./logs2.txt")
log.addHandler(handler)
log.setLevel(1)

@loggerSolveQuadratics(handle=log)
def solve_quadratic(a, b, c):
    logging.info(f"Solving equation: {a}x^2 + {b}x + {c} = 0")

    # Ошибка типов
    for name, value in zip(("a", "b", "c"), (a, b, c)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Parameter '{name}' must be a number, got: {value}")

    # Ошибка: a == 0
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")

    d = b*b - 4*a*c

    if d < 0:
        raise WarningError("Discriminant < 0: no real roots")

    if d == 0:
        x = -b / (2*a)
        return (x,)

    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    return root1, root2, d

solve_quadratic(1, 2, 3)
handler.close()