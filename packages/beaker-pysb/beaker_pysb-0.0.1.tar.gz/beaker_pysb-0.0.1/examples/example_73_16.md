# Description
Demonstrate the use of Kappa stateless generator functions.

# Code
```
pysb.testing import *
pysb import *
pysb.kappa import *

@with_model
def test_kappa_stateless_generator_fxns():
    Monomer('A', ['b'], {'b': ['_1', '_2']})
    Monomer('B', ['b'])
    Rule('A_binds_B', A(b='_1') + B(b=None) >> A(b=('_1', 1)) % B(b=1),
         Parameter('k_A_binds_B', 1))
    Observable('AB', A(b=1) % B(b=1))

    format_monomer_site(A, 'a')
    format_reactionpattern(A(b='_1') + B(b=None))
    format_complexpattern(A(b=('_1', 1)) % B(b=1))
    format_monomerpattern(A(b=1))

```
