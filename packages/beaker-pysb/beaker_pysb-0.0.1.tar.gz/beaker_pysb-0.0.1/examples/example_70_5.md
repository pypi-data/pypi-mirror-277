# Description
This example demonstrates how to use a piecewise expression within a rule to set up and simulate a model using the PySB library.

# Code
```
from pysb import *
from pysb.testing import *
from pysb.bng import *
from pysb.integrate import Solver
import numpy as np

@with_model
def test_piecewise_expression():
    Monomer('A')
    Observable('A_total', A())
    Expression('A_deg_expr', Piecewise((0, A_total < 400.0),
                                       (0.001, A_total < 500.0),
                                       (0.01, True)))
    Initial(A(), Parameter('A_0', 1000))
    Rule('A_deg', A() >> None, A_deg_expr)
    generate_equations(model)
    t = np.linspace(0, 1000, 100)
    sol = Solver(model, t, use_analytic_jacobian=True)

```
