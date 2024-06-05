# Description
Test deep-copying a Model instance with a Parameter component.

# Code
```
copy
pysb.testing import *
pysb.core import *
functools import partial
nose.tools import assert_raises
operator

@with_model
def test_deepcopy_parameter():
    Parameter("a", 1)

```
