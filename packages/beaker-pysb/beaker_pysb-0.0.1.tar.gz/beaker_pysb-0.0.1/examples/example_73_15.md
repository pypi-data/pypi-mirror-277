# Description
Run a Kappa simulation with state values and verify results.

# Code
```
pysb.testing import *
pysb import *

@with_model
def test_kappa_state_values():
    Monomer('A', ['a'], {'a': ['_', '_1', '_2', '_a', 'a']})
    Parameter('k', 1.0)
    Rule('a_synth', None >> A(a='_2'), k)
    Observable('A_', A())


```
