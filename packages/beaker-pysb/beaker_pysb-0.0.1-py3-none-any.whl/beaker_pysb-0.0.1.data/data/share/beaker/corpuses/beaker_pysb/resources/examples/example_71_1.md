# Description
Test BNGL file import by running an ODE simulation on the imported model and the BNGL file directly to compare trajectories.

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

def bngl_import_compare_simulations(bng_file, force=False,
                                    precision=1e-12,
                                    sim_times=range(0, 100, 10)):
    """
    Test BNGL file import by running an ODE simulation on the imported model
    and on the BNGL file directly to compare trajectories.
    """
    m = model_from_bngl(bng_file, force=force)

    if sim_times is None:
        # Skip simulation check
        return

    # Simulate using the BNGL file directly
    with BngFileInterface(model=None) as bng:
        bng.action('readFile', file=bng_file, skip_actions=1)
        bng.action('generate_network')
        bng.action('simulate', method='ode', sample_times=sim_times)
        bng.execute()
        yfull1 = bng.read_simulation_results()

    # Convert to a PySB model, then simulate using BNG
    with BngFileInterface(model=m) as bng:
        bng.action('generate_network')
        bng.action('simulate', method='ode', sample_times=sim_times)
        bng.execute()
        yfull2 = bng.read_simulation_results()

    # Don't check trajectories on forced examples
    if force:
        return

    assert len(yfull1.dtype.names) == len(yfull2.dtype.names)
    for species in yfull1.dtype.names:
        logger.debug(species)
        logger.debug(yfull1[species])
        if species in yfull2.dtype.names:
            renamed_species = species
        else:
            renamed_species = 'Obs_{}'.format(species)
        logger.debug(yfull2[renamed_species])
        assert numpy.allclose(yfull1[species], yfull2[renamed_species],

```
