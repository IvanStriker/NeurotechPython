from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cintegrator.py", annotate=True, compiler_directives={"language_level": 3}),
)