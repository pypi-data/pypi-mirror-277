# Description
How to generate Kappa content from a PySB model using the KappaGenerator class

# Code
```
import pysb
import sympy
import warnings
from sympy.printing import StrPrinter
from sympy.core import S
import collections
import re
import pysb.logging
from pysb.export import (
    CompartmentsNotSupported, LocalFunctionsNotSupported, EnergyNotSupported
) 
# Additional required imports and prelude code from the document

class KappaGenerator(object):
    def __init__(self, model, dialect='kasim', _warn_no_ic=True,
                 _exclude_ic_param=False):
        if model:
            if model.compartments:
                raise CompartmentsNotSupported()
            if model.tags:
                raise LocalFunctionsNotSupported()
            if model.uses_energy:
                raise EnergyNotSupported()
        self.model = model
        self.__content = None
        self.dialect = dialect
        self._warn_no_ic = _warn_no_ic
        self._exclude_ic_param = _exclude_ic_param
        self._renamed_states = collections.defaultdict(dict)
        self._log = pysb.logging.get_logger(__name__)

    def get_content(self):
        if self.__content == None:
            self.generate_content()
        return self.__content

    def generate_content(self):
        self.__content = ''
        #self.generate_compartments()

        # Agent declarations appear to be required in kasim
        # but prohibited in complx
        if (self.dialect == 'kasim'):
            self.generate_molecule_types()
            # Parameters, variables, and expressions are allowed in kasim
            if not self._exclude_ic_param:
                self.generate_parameters()

        self.generate_reaction_rules()
        self.generate_observables()
        if not self._exclude_ic_param:

```
