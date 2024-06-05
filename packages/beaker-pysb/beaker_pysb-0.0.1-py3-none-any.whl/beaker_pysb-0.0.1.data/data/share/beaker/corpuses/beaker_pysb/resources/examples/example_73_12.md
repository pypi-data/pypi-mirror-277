# Description
Demonstrate handling of None in reaction patterns and verify complex pattern parsing.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_none_in_rxn_pat():
    Monomer('A')
    Monomer('B')
    Rule('rule1', A() + None >> None + B(), Parameter('k', 1))
    Initial(A(), Parameter('A_0', 100))
    Observable('B_', B())
    npts = 200
    kres = run_simulation(model, time=100, points=npts, seed=_KAPPA_SEED)

    # check that rule1's reaction pattern parses with ComplexPatterns

```
