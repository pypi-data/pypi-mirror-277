# Description
Simulate a model with a dangling bond and ensure it raises KasimInterfaceError.

# Code
```
pysb.testing import *
pysb import *

@with_model
def test_kappa_error():
    # Model with a dangling bond should raise a KasimInterfaceError
    Monomer('A', ['b'])
    Monomer('B', ['b'])
    Initial(A(b=None), Parameter('A_0', 100))

    # Can't model this as a PySB rule, since it would generate a
    # DanglingBondError. Directly inject kappa code for rule instead.
    assert_raises(KasimInterfaceError, run_simulation, model, time=10,
                  perturbation="'A_binds_B' A(b),B(b) -> A(b!1),B(b) @ "

```
