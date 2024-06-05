# Description
This example demonstrates how to set up and simulate a model with an initial condition expression involving two parameters using the PySB library.

# Code
```
pysb import *
pysb.testing import *
pysb.bng import *
pysb.integrate import Solver

@with_model
def test_ic_expression_with_two_parameters():
    Monomer('A')
    Parameter('k1', 1)
    Parameter('k2', 2)
    Expression('e1', k1*k2)
    Rule('A_deg', A() >> None, k1)
    Initial(A(), e1)
    generate_equations(model)
    t = np.linspace(0, 1000, 100)
    sol = Solver(model, t, use_analytic_jacobian=True)

```
