# Description
Initialize a simple BioNetGen model using PySB including definitions for physical constants, initial concentrations, rate constants, and observables. The example also demonstrates model initialization, parameter setting, expression definitions, monomer specifications, initial conditions, rule creation, and observable declarations.

# Code
```
from __future__ import print_function
from pysb import *


Physical and geometric constants
6.0e23)      # Avogadro's num
0.01)         # scaling factor
f * 1e-10)  # L
f * 3e-12)   # L
Initial concentrations
2e-9)             # nM
EGF_conc * NA * Vo)  # nM
f * 1.8e5)          # copy per cell
Rate constants
9.0e7 / (NA * Vo))  # input /M/sec
0.06)                # /sec
['R'])
['L', 'CR1', 'Y1068'], {'Y1068': ['U', 'P']})
EGF0)
CR1=None, Y1068='U'), EGFR0)
EGF(R=None) + EGFR(L=None) | EGF(R=1) % EGFR(L=1), kp1, km1)
Species LR EGF(R!1).EGFR(L!1)

```
