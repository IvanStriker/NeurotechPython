# Laboratory Work 10
## Structure:
- `integrator.py` - ordinary and async functions for counting integrals
- `cintegrator.py` - the same as the previous, but written in Cython
- `benchmark.py` - code for integrators' speed estimating
- `outcome.txt` - saved result of `benchmark.py`
- `my_decorators.py` - check_types decorator written to test whether a function called with the proper agrs
- `setup_cython.py` - file for compiling `cintegrator.py` into C
- `test_integrator.py` - unit tests
- Other files represent the compiled version of `cintegrator.py`