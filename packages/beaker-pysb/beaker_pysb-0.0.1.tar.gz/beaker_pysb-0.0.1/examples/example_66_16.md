# Description
Test fixed species handling in the `pysb` library.

# Code
```

@with_model
def test_fixed_species():
    Monomer('A', ['a'])
    Monomer('B', ['b'])
    Initial(A(a=1) % B(b=1), Parameter('AB_0', 1), fixed=True)
    Rule('rule1', A(a=1) % B(b=1) >> A(a=None) + B(b=None), Parameter('k', 1))
    generate_equations(model)
    num_non_zeros = model.stoichiometry_matrix[0].getnnz()

```
