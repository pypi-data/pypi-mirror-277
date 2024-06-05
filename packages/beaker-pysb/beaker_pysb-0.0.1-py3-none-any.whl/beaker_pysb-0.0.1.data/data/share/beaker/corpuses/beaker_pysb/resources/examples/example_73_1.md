# Description
Run a Kappa simulation with a basic binding/unbinding model for two monomers and verify simulation results.

# Code
```
pysb.testing import *
pysb import *

@with_model
def test_kappa_simulation_results():
    Monomer('A', ['b'])
    Monomer('B', ['b'])
    Initial(A(b=None), Parameter('A_0', 100))
    Initial(B(b=None), Parameter('B_0', 100))
    Rule('A_binds_B', A(b=None) + B(b=None) >> A(b=1) % B(b=1),
         Parameter('kf', 1))
    Rule('A_binds_B_rev', A(b=1) % B(b=1) >> A(b=None) + B(b=None),
         Parameter('kr', 1))
    Observable('AB', A(b=1) % B(b=1))
    npts = 200
    kres = run_simulation(model, time=100, points=npts, seed=_KAPPA_SEED)
    ok_(len(kres['time']) == npts + 1)
    ok_(len(kres['AB']) == npts + 1)
    ok_(kres['time'][0] == 0)

```
