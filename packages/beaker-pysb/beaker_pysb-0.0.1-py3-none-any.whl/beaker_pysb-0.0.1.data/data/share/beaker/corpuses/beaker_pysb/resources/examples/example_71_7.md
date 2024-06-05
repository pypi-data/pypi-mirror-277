# Description
Test for the expected error behavior when importing BNGL files that are expected to generate specific errors.

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

def test_bngl_import_expected_errors():
    errtype = {'ratelawtype': 'Rate law \w* has unknown type',
               'ratelawmissing': 'Rate law missing for rule',
               'plusminus': 'PLUS/MINUS state values',
               'statelabels': 'BioNetGen component/state labels are not yet supported',
              }
    expected_errors = {'ANx': errtype['plusminus'],
                       'CaOscillate_Sat': errtype['ratelawtype'],
                       'heise': errtype['statelabels'],
                       'isingspin_energy': errtype['ratelawmissing'],
                       'test_MM': errtype['ratelawtype'],
                       'test_sat': errtype['ratelawtype'],
                       }

    for filename, errmsg in expected_errors.items():
        full_filename = _bngl_location(filename)
        yield (assert_raises_regex,
               BnglImportError,
               errmsg,
               bngl_import_compare_simulations,

```
