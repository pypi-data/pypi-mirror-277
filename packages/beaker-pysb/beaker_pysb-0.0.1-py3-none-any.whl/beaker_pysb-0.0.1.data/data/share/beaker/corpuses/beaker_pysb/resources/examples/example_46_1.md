# Description
Setting up a biochemical pathway using PySB including the declaration of molecules, their parameters, and the defining of reaction rules and observables.

# Code
```
from pysb import *
from pysb.macros import *
from scipy.constants import N_A

Model()

Parameter('vol', 1e-20)
NA_V = N_A * vol.value
Parameter('k1', 0.015 * NA_V)
Parameter('k2', 0)
Parameter('k3', 200 / NA_V)
Parameter('k4', 2 * 180 / NA_V / NA_V)
Parameter('kp4', 0.018)
Parameter('k5', 0)
Parameter('k6', 1.0)
Parameter('k7', 0.6)
Parameter('k8', 1e6)
Parameter('k9', 1e3)
Monomer('cyclin', ['Y', 'b'], {'Y': ['U', 'P']})

Rule 1
b=None), k1)
Rule 2
b=None), k2)
Rule 3
cyclin(Y='U', b=None) + cdc2(Y='P', b=None) >> cyclin(Y='P', b=1) % cdc2(Y='P', b=1), k3)
Rule 4
cyclin(Y='P', b=1) % cdc2(Y='P', b=1) >> cyclin(Y='P', b=1) % cdc2(Y='U', b=1), kp4)
Rule 4'
cyclin(Y='P', b=1) % cdc2(Y='P', b=1) + cyclin(Y='P', b=2) % cdc2(Y='U', b=2) + cyclin(Y='P', b=2) % cdc2(Y='U', b=2) >>
b=1) % cdc2(Y='U', b=1) + cyclin(Y='P', b=2) % cdc2(Y='U', b=2) + cyclin(Y='P', b=2) % cdc2(Y='U', b=2), k4)
Rule 5
cyclin(Y='P', b=1) % cdc2(Y='U', b=1) >> cyclin(Y='P', b=1) % cdc2(Y='P', b=1), k5)
Rule 6
cyclin(Y='P', b=1) % cdc2(Y='U', b=1) >> cyclin(Y='P', b=None) + cdc2(Y='U', b=None), k6)
cyclin(Y='P', b=1) % cdc2(Y='U', b=1) >> cdc2(Y='U', b=None), k6)
Rule 7
b=None), k7)
Rules 8 and 9
b=None), cdc2(Y='P', b=None), [k8, k9])
cyclin()) # Total Cyclin
cdc2()) # Total CDC2
cyclin(Y='P', b=1) % cdc2(Y='U', b=1) ) # Active Complex
cdc2(Y='U', b=None))
cdc2(Y='P', b=None))
cdc2(Y='U', b=1) % cyclin(Y='P', b=1))
cdc2(Y='P', b=1) % cyclin(Y='P', b=1))
cyclin(Y='U', b=None))
cyclin(Y='P', b=None))
[C2] in Tyson
1*NA_V)
Parameter("cdc0", 1.0)
b=None), cdc0)
[Y] in Tyson
0.25*NA_V)
Parameter('cyc0', 0.25)

```
