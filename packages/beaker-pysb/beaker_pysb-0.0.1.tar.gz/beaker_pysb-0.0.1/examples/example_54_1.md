# Description
Convert a BioNetGen .bngl model file into a PySB Model.

# Code
```
from pysb.builder import Builder
from pysb.bng import BngFileInterface
import xml.etree.ElementTree as ET
import re
import warnings
import pysb.logging
import collections
import numbers

def model_from_bngl(filename, force=False, cleanup=True):
    """
    Convert a BioNetGen .bngl model file into a PySB Model.

    Notes
    -----

    The following features are not supported in PySB and will cause an error
    if present in a .bngl file:

    * Fixed species (with a ``$`` prefix, like ``$Null``)
    * BNG excluded or included reaction patterns (deprecated in BNG)
    * BNG local functions
    * Molecules with identically named sites, such as ``M(l,l)``
    * BNG's custom rate law functions, such as ``MM`` and ``Sat``
      (deprecated in BNG)

    Parameters
    ----------
    filename : string
        A BioNetGen .bngl file
    force : bool, optional
        The default, False, will raise an Exception if there are any errors
        importing the model to PySB, e.g. due to unsupported features.
        Setting to True will attempt to ignore any import errors, which may
        lead to a model that only poorly represents the original. Use at own
        risk!
    cleanup : bool
        Delete temporary directory on completion if True. Set to False for
        debugging purposes.
    """
    bb = BnglBuilder(filename, force=force, cleanup=cleanup)

```
