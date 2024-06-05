# Description
Generate an influence map using static analysis and verify its type.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_run_static_analysis_imap():
    """Test generation of influence map by run_static_analysis"""
    Monomer('A', [])
    Monomer('B', ['active'], {'active': ['y', 'n']})
    Monomer('C', ['active'], {'active': ['y', 'n']})
    Initial(A(), Parameter('A_0', 100))
    Initial(B(active='n'), Parameter('B_0', 100))
    Initial(C(active='n'), Parameter('C_0', 100))
    Rule('A_activates_B',
         A() + B(active='n') >> A() + B(active='y'),
         Parameter('k_A_activates_B', 1))
    Rule('B_activates_C',
         B(active='y') + C(active='n') >> B(active='y') + C(active='y'),
         Parameter('k_B_activates_C', 1))
    res = run_static_analysis(model, contact_map=False, influence_map=True)

```
