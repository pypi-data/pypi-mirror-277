# Description
Run a Kappa simulation with flux map generation and verify the results.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_flux_map():
    """Test kappa simulation with flux map (returns tuple with graph)"""
    Monomer('A', ['b'])
    Monomer('B', ['a', 'c'])
    Monomer('C', ['b'])
    Parameter('k', 0.001)
    Rule('A_binds_B', A(b=None) + B(a=None) >> A(b=1) % B(a=1), k)
    Rule('C_binds_B', C(b=None) + B(c=None) >> C(b=1) % B(c=1), k)
    Observable('ABC', A(b=1) % B(a=1, c=2) % C(b=2))
    Initial(A(b=None), Parameter('A_0', 100))
    Initial(B(a=None, c=None), Parameter('B_0', 100))
    Initial(C(b=None), Parameter('C_0', 100))
    res = run_simulation(model, time=10, points=100, flux_map=True,
                         cleanup=True, seed=_KAPPA_SEED, verbose=False)
    simdata = res.timecourse
    ok_(len(simdata['time']) == 101)
    ok_(len(simdata['ABC']) == 101)
    ok_(simdata['time'][0] == 0)
    ok_(sorted(simdata['time'])[-1] == 10)
    fluxmap = res.flux_map

```
