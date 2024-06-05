# Description
Test bidirectional rules collapse in the `pysb` library.

# Code
```

@with_model
def test_bidirectional_rules_collapse():
    Monomer('A')
    Monomer('B')
    Initial(B(), Parameter('B_init', 0))
    Initial(A(), Parameter('A_init', 100))
    Rule('Rule1', B() | A(), Parameter('k3', 10), Parameter('k1', 1))
    Rule('Rule2', A() | B(), k1, Parameter('k2', 1))
    Rule('Rule3', B() >> A(), Parameter('k4', 5))
    generate_equations(model)
    ok_(len(model.reactions) == 4)
    ok_(len(model.reactions_bidirectional) == 1)
    ok_(len(model.reactions_bidirectional[0]['rule']) == 3)

```
