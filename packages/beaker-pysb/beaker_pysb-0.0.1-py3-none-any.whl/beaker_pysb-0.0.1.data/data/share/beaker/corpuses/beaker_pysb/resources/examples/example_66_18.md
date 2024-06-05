# Description
Test multi-bonds between monomers in the `pysb` library.

# Code
```

@with_model
def test_multibonds():
    Monomer('A', ['a'])
    Monomer('B', ['b'])
    Parameter('k1', 100)
    Parameter('A_0', 200)
    Parameter('B_0', 50)
    Rule('r1', A(a=None) + A(a=None) + B(b=None) >>
            A(a=1) % A(a=[1, 2]) % B(b=2), k1)
    Initial(A(a=None), A_0)
    Initial(B(b=None), B_0)

    generate_equations(model)

    assert model.species[2].is_equivalent_to(
        A(a=1) % A(a=[1, 2]) % B(b=2)

```
