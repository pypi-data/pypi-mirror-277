# Description
Test bidirectional rules in the `pysb` library.

# Code
```

@with_model
def test_bidirectional_rules():
    Monomer('A')
    Monomer('B')
    Initial(A(), Parameter('A_init', 100))
    Rule('Rule1', A() | B(), Parameter('k1', 1), Parameter('k2', 1))
    Rule('Rule2', B() >> A(), Parameter('k3', 10))
    Rule('Rule3', B() >> A(), Parameter('k4', 5))
    generate_equations(model)
    ok_(len(model.reactions) == 4)
    ok_(len(model.reactions_bidirectional) == 1)
    ok_(len(model.reactions_bidirectional[0]['rule']) == 3)

```
