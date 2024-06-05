# Description
Generate and validate a network with appropriate initial conditions and rules using `pysb` library.

# Code
```
pysb.testing import *
pysb import *
pysb.bng import *

@with_model
def test_generate_network():
    Monomer('A')
    assert_raises((NoInitialConditionsError, NoRulesError),
                  generate_network, model)
    Parameter('A_0', 1)
    Initial(A(), A_0)
    assert_raises(NoRulesError, generate_network, model)
    Parameter('k', 1)
    Rule('degrade', A() >> None, k)

```
