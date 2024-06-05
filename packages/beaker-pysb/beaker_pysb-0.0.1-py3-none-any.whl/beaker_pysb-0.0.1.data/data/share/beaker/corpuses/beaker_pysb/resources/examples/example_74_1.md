# Description
Example demonstrating the use of the 'catalyze_one_step' macro in PySB, including setting up monomers and verifying the creation of rules in the model.

# Code
```
pysb.testing import *
pysb.core import *

@with_model
def test_catalyze_one_step_None():
    # What if no substrate is required, hand-wavy, but present in published models!
    Monomer('E', ['b'])
    Monomer('P')
    catalyze_one_step(E, None, P, 1e-4)

```
