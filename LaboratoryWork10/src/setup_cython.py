from setuptools import setup
from Cython.Build import cythonize

setup(
    name="cintegrator",
    ext_modules=cythonize("cintegrator.pyx", annotate=True,
                          compiler_directives={"language_level": 3}),
)