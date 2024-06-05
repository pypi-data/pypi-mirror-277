# Description
Display a ValueError when running static analysis on an invalid model.

# Code
```
pysb.testing import *
pysb import *

@raises(ValueError)
@with_model
def test_run_static_analysis_valueerror():
    Monomer('A', ['b'])
    Monomer('B', ['b'])
    Rule('A_binds_B', A(b=None) + B(b=None) >> A(b=1) % B(b=1),
         Parameter('k_A_binds_B', 1))
    Observable('AB', A(b=1) % B(b=1))

```
