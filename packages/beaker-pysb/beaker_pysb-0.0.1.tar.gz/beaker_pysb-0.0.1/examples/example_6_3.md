# Description
Generating the contact map via KaSa for a given model.

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

def contact_map(model, **kwargs):
    """Generates the contact map via KaSa.

    Parameters
    ----------
    model : pysb.core.Model
        The model for generating the influence map.
    **kwargs : other keyword arguments
        Any other keyword arguments are passed to the function
        :py:func:`run_static_analysis`.

    Returns
    -------
    networkx MultiGraph object containing the contact map. For details on
    viewing the contact map graphically see :func:`run_static_analysis` (notes
    section).
    """
    kasa_result = run_static_analysis(model, influence_map=False,
                                    contact_map=True, **kwargs)

```
