# Description
Wrapper method for running cupSODA simulations using the `CupSodaSimulator` class. This example demonstrates how to set up the simulator with a model and time span, specify initial conditions and parameters, and run the simulations to obtain the results.

# Code
```
from pysb.simulator.base import Simulator, SimulatorException, SimulationResult
import pysb
import pysb.bng
import numpy as np
from scipy.constants import N_A
import os
import re
import subprocess
import tempfile
import time
import logging
from pysb.logging import EXTENDED_DEBUG
import shutil
from pysb.pathfinder import get_path
import sympy
import collections
from collections.abc import Iterable
try:
    import pandas as pd
except ImportError:
    pd = None
try:
    import pycuda.driver as cuda
except ImportError:
    cuda = None

class CupSodaSimulator(Simulator):
    # (Class definition goes here, with all necessary imports and attributes)
    
    def __init__(self, model, tspan=None, initials=None, param_values=None, verbose=False, **kwargs):
        # (Constructor implementation goes here)

    def run(self, tspan=None, initials=None, param_values=None):

def run_cupsoda(model, tspan, initials=None, param_values=None,
                integrator='cupsoda', cleanup=True, verbose=False, **kwargs):
    """Wrapper method for running cupSODA simulations.
    
    Parameters
    ----------
    See ``CupSodaSimulator`` constructor.
    
    Returns
    -------
    SimulationResult.all : list of record arrays
        List of trajectory sets. The first dimension contains species,
        observables and expressions (in that order)
    """
    sim = CupSodaSimulator(model, tspan=tspan, integrator=integrator,
                           cleanup=cleanup, verbose=verbose, **kwargs)
    simres = sim.run(initials=initials, param_values=param_values)

```
