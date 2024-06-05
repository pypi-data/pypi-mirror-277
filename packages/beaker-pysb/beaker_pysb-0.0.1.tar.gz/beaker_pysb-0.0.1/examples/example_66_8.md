# Description
Test reversible synthesis and degradation in the `pysb` library.

# Code
```

@with_model
def test_reversible_synth_deg():
    Monomer('A')
    Parameter('k_synth', 2.0)
    Parameter('k_deg', 1.0)
    Rule('synth_deg', A() | None, k_deg, k_synth)
    assert synth_deg.is_synth()
    assert synth_deg.is_deg()

```
