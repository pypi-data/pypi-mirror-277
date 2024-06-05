# Description
Test for the expected behavior when importing a BioModels file using a mock function.

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
}

def _sbml_location(filename):
    return os.path.join(_bng_validate_directory(), 'INPUT_FILES', filename + '.xml')

def _sbml_for_mocks(accession_no, mirror):
    _, filename = tempfile.mkstemp()
    shutil.copy(_sbml_location('test_sbml_flat_SBML'), filename)

@mock.patch('pysb.importers.sbml._download_biomodels', _sbml_for_mocks)
def test_biomodels_import_with_mock():

```
