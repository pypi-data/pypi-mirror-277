# Description
This example shows how to use an observable within an expression to set up and simulate a model using the PySB library.

# Code
```
pysb import *
pysb.testing import *
pysb.bng import *
pysb.integrate import Solver

@with_model
def test_expressions_with_one_observable():
    Monomer('A')
    Parameter('k1', 1)
    Observable('o1', A())
    Expression('e1', o1)
    Rule('A_deg', A() >> None, k1)
    Initial(A(), k1)
    generate_equations(model)
    t = np.linspace(0, 1000, 100)
    sol = Solver(model, t, use_analytic_jacobian=True)

```
