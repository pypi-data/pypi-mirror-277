# Description
Run a Kappa simulation with unicode characters in Monomer, Rule, Parameter, Initial, and Observable definitions.

# Code
```
pysb.testing import *
pysb import *

@with_model
def test_unicode_strs():
    Monomer(u'A', [u'b'], {u'b':[u'y', u'n']})
    Rule(u'rule1', A(b=u'y') >> A(b=u'n'),
         Parameter(u'k', 1))
    Initial(A(b=u'y'), Parameter(u'A_0', 100))
    Observable(u'A_y', A(b=u'y'))
    npts = 200

```
