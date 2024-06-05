# Description
Test BNGL file import by running a network-free simulation (NFSim) on the imported model and the BNGL file directly to compare trajectories.

# Code
```
import os
import pysb.pathfinder as pf
from pysb.bng import BngFileInterface
from pysb.importers.bngl import model_from_bngl, BnglImportError
from pysb.importers.sbml import model_from_sbml, model_from_biomodels
import numpy
from nose.tools import assert_raises_regex, raises
import warnings
import mock
import tempfile
import shutil
from pysb.logging import get_logger

logger = get_logger(__name__)

# Some models don't match BNG originals exactly due to loss of numerical precision. See https://github.com/pysb/pysb/issues/443
REDUCED_PRECISION = {
    'CaOscillate_Func': 1e-4,
    'michment': 1e-8,
    'motor': 1e-8,
    'Repressilator': 1e-11,

def bngl_import_compare_nfsim(bng_file):
    m = model_from_bngl(bng_file)

    BNG_SEED = 123

    # Simulate using the BNGL file directly
    with BngFileInterface(model=None) as bng:
        bng.action('readFile', file=bng_file, skip_actions=1)
        bng.action('simulate', method='nf', n_steps=10, t_end=100,
                   seed=BNG_SEED)
        bng.execute()
        yfull1 = bng.read_simulation_results()

    # Convert to a PySB model, then simulate using BNG
    with BngFileInterface(model=m) as bng:
        bng.action('simulate', method='nf', n_steps=10, t_end=100,
                   seed=BNG_SEED)
        bng.execute()
        yfull2 = bng.read_simulation_results()

    # Check all species trajectories are equal (within numerical tolerance)
    for i in range(len(m.observables)):
        print(i)
        print(yfull1[i])
        print(yfull2[i])
        print(yfull1[i] == yfull2[i])

```
