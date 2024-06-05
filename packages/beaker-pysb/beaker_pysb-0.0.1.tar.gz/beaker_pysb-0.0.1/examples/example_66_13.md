# Description
Test parameters named after a SymPy function in the `pysb` library.

# Code
```

@with_model
def test_sympy_parameter_keyword():
    Monomer('A')
    Initial(A(), Parameter('A_0', 100))
    Parameter('deg', 10)  # deg is a sympy function
    Rule('Rule1', A() >> None, deg)

```
