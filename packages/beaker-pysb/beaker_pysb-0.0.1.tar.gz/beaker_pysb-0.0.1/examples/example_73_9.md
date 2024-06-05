# Description
Generate a contact map and verify its type.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_contact_map():
    Monomer('A', ['b'])
    Monomer('B', ['b'])
    Rule('A_binds_B', A(b=None) + B(b=None) >> A(b=1) % B(b=1),
         Parameter('k_A_binds_B', 1))
    Observable('AB', A(b=1) % B(b=1))
    res = contact_map(model, cleanup=True)

```
