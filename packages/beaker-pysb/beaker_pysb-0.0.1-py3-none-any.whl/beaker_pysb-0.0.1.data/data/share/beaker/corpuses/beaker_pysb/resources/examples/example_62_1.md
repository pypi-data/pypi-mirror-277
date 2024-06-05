# Description
Simulate a model using ScipyOdeSimulator and display the results for the observable 'A_total'.

# Code
```
from pysb.simulator.base import Simulator, SimulationResult
import scipy.integrate, scipy.sparse
from sympy.utilities.autowrap import CythonCodeWrapper
from sympy.utilities.codegen import C99CodeGen, Routine, InputArgument, OutputArgument, default_datatypes
import distutils
import pysb.bng
import sympy
import re
from functools import partial
import numpy as np
import warnings
import os
import inspect
from pysb.logging import get_logger, PySBModelLoggerAdapter, EXTENDED_DEBUG
import logging
import contextlib
import importlib
template
import shutil
from concurrent.futures import ProcessPoolExecutor, Executor, Future

class ScipyOdeSimulator(Simulator):
    ...  # Insert the entire class code provided.

# Additional required logging context manager and helper methods
@contextlib.contextmanager
def _patch_distutils_logging(base_logger):
    ...

@contextlib.contextmanager
def _set_cflags_no_warnings(logger):
    ...

class _DistutilsProxyLoggerAdapter(logging.LoggerAdapter):
    ...

def _integrator_process(initials, param_values, tspan, integrator_name, integrator_opts, rhs_builder):
    ...

class RhsBuilder:
    ...

class PythonRhsBuilder(RhsBuilder):
    ...

class CythonRhsBuilder(RhsBuilder):
    ...

_rhs_builders = {
    'cython': CythonRhsBuilder,
    'python': PythonRhsBuilder
}

def _select_rhs_builder(compiler, logger):
    ...

class SerialExecutor(Executor):

>>> from pysb.examples.robertson import model
>>> import numpy as np
>>> np.set_printoptions(precision=4)
>>> sim = ScipyOdeSimulator(model, tspan=np.linspace(0, 40, 10))
>>> simulation_result = sim.run()
>>> print(simulation_result.observables['A_total']) \
    #doctest: +NORMALIZE_WHITESPACE
[1.      0.899   0.8506  0.8179  0.793   0.7728  0.7557  0.7408  0.7277

```
