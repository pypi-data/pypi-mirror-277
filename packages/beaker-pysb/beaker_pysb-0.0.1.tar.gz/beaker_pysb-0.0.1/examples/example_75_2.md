# Description
This example shows how to use wildcards in patterns and match them against monomer patterns using the match_complex_pattern function.

# Code
```
from pysb import as_complex_pattern, Monomer

def test_wildcards():
    a_wild = as_complex_pattern(Monomer('A', ['b'], _export=False)(b=WILD))
    b_mon = as_complex_pattern(Monomer('B', _export=None))

    # B() should not match A(b=WILD)

```
