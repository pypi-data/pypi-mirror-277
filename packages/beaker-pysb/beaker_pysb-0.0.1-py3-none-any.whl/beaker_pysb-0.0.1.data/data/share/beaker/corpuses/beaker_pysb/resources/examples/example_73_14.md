# Description
Run a Kappa simulation with two ghost agents and demonstrate reaction pattern addition.

# Code
```
pysb.testing import *
pysb import *

@with_model
def test_kappa_two_ghost_agents():
    Monomer('A')
    Monomer('M')
    Parameter('k', 3.0)
    Rule('synthesize_A_and_B', M() + None + None >> M() + A() + A(), k)
    Initial(M(), Parameter('M_0', 1000))
    Observable('A_', A())

    # check the ReactionPattern.__radd__ version
    rp = None + (None + A())
    assert len(rp.complex_patterns) == 3


```
