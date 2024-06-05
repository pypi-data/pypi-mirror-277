# Description
Generate a contact map using static analysis and verify its type.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_run_static_analysis_cmap():
    """Test generation of contact map by run_static_analysis"""
    Monomer('A', ['b'])
    Monomer('B', ['b'])
    Rule('A_binds_B', A(b=None) + B(b=None) >> A(b=1) % B(b=1),
         Parameter('k_A_binds_B', 1))
    Observable('AB', A(b=1) % B(b=1))
    res = run_static_analysis(model, contact_map=True, influence_map=False)
    ok_(isinstance(res.contact_map, nx.MultiGraph))

```
