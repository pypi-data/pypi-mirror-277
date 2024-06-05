# Description
Handle parameter name overlap in Kappa simulations.

# Code
```
pysb.testing import *
pysb import *

@with_model
def test_kappa_parameter_name_overlap():
    Parameter('avogadro', 6.022e23)
    Parameter('cell_volume', 2.25e-12)
    Parameter('cell_volume_fraction', 0.001)
    Expression('stochastic', avogadro * cell_volume * cell_volume_fraction)

    Monomer('A', ['b'])
    Initial(A(b=None), Parameter('A_0', 100))
    Rule('deg_A', A(b=None) >> None, stochastic)
    Observable('A_', A())

```
