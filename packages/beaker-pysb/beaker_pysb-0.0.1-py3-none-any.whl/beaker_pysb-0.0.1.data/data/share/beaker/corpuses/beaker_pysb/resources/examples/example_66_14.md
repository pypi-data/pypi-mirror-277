# Description
Test using logarithmic expressions in the `pysb` library.

# Code
```
from pysb import *

@with_model
def test_log():
    Monomer('A')
    Expression('expr1', sympy.log(100))
    Rule('Rule1', None >> A(), expr1)

```
