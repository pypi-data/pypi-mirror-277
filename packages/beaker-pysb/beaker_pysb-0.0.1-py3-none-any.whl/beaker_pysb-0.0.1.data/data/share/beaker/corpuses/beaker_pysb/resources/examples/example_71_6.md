# Description
Test for the expected behavior when importing BNGL files that are expected to pass.

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

def test_bngl_import_expected_passes():
    for filename in ('CaOscillate_Func',
                     'continue',
                     'deleteMolecules',
                     'egfr_net',
                     'empty_compartments_block',
                     'gene_expr',
                     'gene_expr_func',
                     'gene_expr_simple',
                     'isomerization',
                     'localfunc',
                     'michment',
                     'Motivating_example_cBNGL',
                     'motor',
                     'simple_system',
                     'test_compartment_XML',
                     'test_setconc',
                     'test_synthesis_cBNGL_simple',
                     'test_synthesis_complex',
                     'test_synthesis_complex_0_cBNGL',
                     'test_synthesis_complex_source_cBNGL',
                     'test_synthesis_simple',
                     'toy-jim',
                     'univ_synth',
                     'visualize',
                     'Repressilator',
                     'fceri_ji',
                     'test_paramname',
                     'tlmr'):
        full_filename = _bngl_location(filename)
        yield (bngl_import_compare_simulations, full_filename, False,

```
