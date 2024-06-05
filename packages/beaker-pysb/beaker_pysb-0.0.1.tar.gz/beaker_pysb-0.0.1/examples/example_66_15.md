# Description
Ensure generating equations catches BNG-specific errors in `pysb` library.

# Code
```
pysb import *
pysb.bng import BngInterfaceError

@with_model
def test_bng_error():
    Monomer('A', ['a'], {'a': ['s1', 's2']})
    Parameter('A_0', 100)
    Initial(A(a='s1'), A_0)
    Parameter('kf', 1)
    # The following rule does not specify A's site on the RHS, so should generate a BNG error
    Rule('r1', A(a='s1') >> A(), kf)
    assert_raises_regex(
        BngInterfaceError,
        'Molecule created in reaction rule: Component\(s\) a missing from molecule A\(\)',
        generate_equations,
        model

```
