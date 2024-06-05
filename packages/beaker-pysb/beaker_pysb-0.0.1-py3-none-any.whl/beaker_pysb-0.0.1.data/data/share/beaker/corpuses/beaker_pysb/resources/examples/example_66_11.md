# Description
Check unicode strings handling in the `pysb` library.

# Code
```

@with_model
def test_unicode_strs():
    Monomer(u'A', [u'b'], {u'b':[u'y', u'n']})
    Monomer(u'B')
    Rule(u'rule1', A(b=u'y') >> B(), Parameter(u'k', 1))
    Initial(A(b=u'y'), Parameter(u'A_0', 100))

```
