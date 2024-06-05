# Description
Ensure `None` in reaction patterns works correctly in the `pysb` library.

# Code
```

@with_model
def test_none_in_rxn_pat():
    Monomer(u'A', [u'b'], {u'b': [u'y', u'n']})
    Monomer(u'B')
    Rule(u'rule1', A(b=u'y') + None >> None + B(),
         Parameter(u'k', 1))
    Initial(A(b=u'y'), Parameter(u'A_0', 100))

```
