# Description
This example demonstrates how to create nested expressions and use them in rules to set up and simulate a model using the PySB library.

# Code
```
pysb import *
pysb.testing import *
pysb.bng import *
pysb.integrate import Solver

@with_model
def test_nested_expression():
    Monomer(u'A')
    Monomer(u'B')
    Parameter(u'k1', 1)
    Observable(u'o1', B())
    Expression(u'e1', o1*k1)
    Expression(u'e2', e1+5)
    Initial(A(), Parameter(u'A_0', 1000))
    Initial(B(), Parameter(u'B_0', 1))
    Rule(u'A_deg', A() >> None, e2)
    generate_equations(model)
    t = np.linspace(0, 1000, 100)
    sol = Solver(model, t, use_analytic_jacobian=True)

```
