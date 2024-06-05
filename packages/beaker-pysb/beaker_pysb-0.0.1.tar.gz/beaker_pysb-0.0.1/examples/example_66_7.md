# Description
Test zero-order synthesis without initial conditions in the `pysb` library.

# Code
```

@with_model
def test_zero_order_synth_no_initials():
    Monomer('A')
    Monomer('B')
    Rule('Rule1', None >> A(), Parameter('ksynth', 100))
    Rule('Rule2', A() | B(), Parameter('kf', 10), Parameter('kr', 1))

```
