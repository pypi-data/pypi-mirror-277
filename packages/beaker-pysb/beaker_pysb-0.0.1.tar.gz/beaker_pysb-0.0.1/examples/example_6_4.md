# Description
Generating the influence map via KaSa for a given model.

# Code
```
import pysb.pathfinder as pf
from pysb.generator.kappa import KappaGenerator
import os
import subprocess
import tempfile
shutil
import warnings
from collections import namedtuple
from pysb.util import read_dot
import pysb.logging

logger = pysb.logging.get_logger(__name__)

StaticAnalysisResult = namedtuple('StaticAnalysisResult', ['contact_map', 'influence_map'])

def run_static_analysis(model, influence_map=False, contact_map=False, cleanup=True, output_prefix=None, output_dir=None, verbose=False):
    # Implementation of run_static_analysis function

def influence_map(model, **kwargs):
    """Generates the influence map via KaSa.

    Parameters
    ----------
    model : pysb.core.Model
        The model for generating the influence map.
    **kwargs : other keyword arguments
        Any other keyword arguments are passed to the function
        :py:func:`run_static_analysis`.

    Returns
    -------
    networkx MultiGraph object containing the influence map. For details on
    viewing the influence map graphically see :func:`run_static_analysis`
    (notes section).
    """

    kasa_result = run_static_analysis(model, influence_map=True,
                                    contact_map=False, **kwargs)

```
