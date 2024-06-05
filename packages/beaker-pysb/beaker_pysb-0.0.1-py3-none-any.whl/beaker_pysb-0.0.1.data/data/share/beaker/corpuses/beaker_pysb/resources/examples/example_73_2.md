# Description
Showcase the usage of various sympy expressions in a Kappa simulation.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_kappa_expressions():
    Monomer('A',['site'],{'site': ['u']})
    Parameter('two',2)
    Parameter('kr',0.1)
    Parameter('num_A',1000)
    Expression('kf',1e-5/two)
    Expression('test_sqrt', -1 + sympy.sqrt(1 + two))
    Expression('test_pi', sympy.pi)
    Expression('test_e', sympy.E)
    Expression('test_log', sympy.log(two))
    Expression('test_exp', sympy.exp(two))
    Expression('test_sin', sympy.sin(two))
    Expression('test_cos', sympy.cos(two))
    Expression('test_tan', sympy.tan(two))
    Expression('test_max', sympy.Max(two, kr, 2.0))
    Expression('test_min', sympy.Min(two, kr, 2.0))
    Expression('test_mod', sympy.Mod(10, two))
    Expression('test_piecewise', sympy.Piecewise((0.0, two < 400.0),
                                                 (1.0, True)))
    Initial(A(site=('u')),num_A)
    Rule('dimerize_fwd',
         A(site='u') + A(site='u') >> A(site=('u', 1)) % A(site=('u',1)), kf)
    Rule('dimerize_rev',
         A(site=('u', 1)) % A(site=('u',1)) >>
         A(site='u') + A(site='u'), kr)
    # We need an arbitrary observable here to get a Kappa output file
    Observable('A_obs', A())
    # Accommodates Expression in kappa simulation
    run_simulation(model, time=0)

    Rule('degrade_dimer', A(site=('u', ANY)) >> None, kr)
    Observable('dimer', A(site=('u', ANY)))
    # Accommodates site with explicit state and arbitrary bond

```
