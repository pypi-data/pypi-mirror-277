# Description
Test energy pattern usage in the `pysb` library.

# Code
```

@with_model
def test_energy():
    Monomer('A', ['a', 'b'])
    Monomer('B', ['a'])
    Parameter('RT', 2)
    Parameter('A_0', 10)
    Parameter('AB_0', 10)
    Parameter('phi', 0)
    Expression('E_AAB_RT', -5 / RT)
    Expression('E0_AA_RT', -1 / RT)
    Rule(
        'A_dimerize',
        A(a=None) + A(a=None) | A(a=1) % A(a=1),
        phi,
        E0_AA_RT,
        energy=True,
    )
    EnergyPattern('epAAB', A(a=1) % A(a=1, b=2) % B(a=2), E_AAB_RT)
    Initial(A(a=None, b=None), A_0)
    Initial(A(a=None, b=1) % B(a=1), AB_0)

    generate_equations(model)


```
