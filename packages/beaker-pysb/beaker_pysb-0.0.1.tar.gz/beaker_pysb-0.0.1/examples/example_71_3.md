# Description
Test for the expected behavior when importing BNGL files that are expected to pass with force.

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

def test_bngl_import_expected_passes_with_force():
    for filename in ('Haugh2b',
                     'Motivating_example',
                     ):
        full_filename = _bngl_location(filename)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')

```
