# Description
Test multi-state species handling in the `pysb` library.

# Code
```
from pysb import *

@with_model
def test_multistate():
    Monomer('A', ['a', 'a'], {'a': ['u', 'p']})
    Parameter('k1', 100)
    Parameter('A_0', 200)
    Rule('r1', None >> A(a=MultiState('u', 'p')), k1)
    Initial(A(a=MultiState(('u', 1), 'p')) %
            A(a=MultiState(('u', 1), 'u')), A_0)

    generate_equations(model)

    assert model.species[0].is_equivalent_to(
        A(a=MultiState(('u', 1), 'p')) % A(a=MultiState(('u', 1), 'u')))
    assert model.species[1].is_equivalent_to(

```
