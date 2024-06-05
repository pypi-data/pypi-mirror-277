# Description
Test invalid state assignments in Monomer and MonomerPattern calls.

# Code
```
copy
pysb.testing import *
pysb.core import *
functools import partial
nose.tools import assert_raises
operator

@with_model
def test_invalid_state():
    Monomer('A', ['a', 'b'], {'a': ['a1', 'a2'], 'b': ['b1']})
    # Specify invalid state in Monomer.__call__
    assert_raises(ValueError, A, a='spam')
    # Specify invalid state in MonomerPattern.__call__

```
