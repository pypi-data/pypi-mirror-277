# Description
This example illustrates how to use the `MatchOnce` function to ensure that a pattern only matches once per species, even if it could match multiple times within that species. This is useful for adjusting reaction rate multiplicity to prevent a species from degrading or reacting faster than desired when it contains multiple identical molecules.

# Code
```
import sympy
import networkx as nx
from collections.abc import Iterable

class Component:
    pass

class Model:
    pass

class Rule(object):
    def __init__(self, name, reactant, product, k):
        self.name = name
        self.reactant = reactant
        self.product = product
        self.k = k

def as_complex_pattern(pattern):
    # This is a mock implementation. The real one should convert pattern to ComplexPattern.

def MatchOnce(pattern):
    """
    Make a ComplexPattern match-once.

    ``MatchOnce`` adjusts reaction rate multiplicity by only counting a pattern
    match once per species, even if it matches within that species multiple
    times.

    For example, if one were to have molecules of ``A`` degrading with a
    specified rate:

    >>> Rule('A_deg', A() >> None, kdeg)                # doctest: +SKIP

    In the situation where multiple molecules of ``A()`` were present in a
    species (e.g. ``A(a=1) % A(a=1)``), the above ``A_deg`` rule would have
    multiplicity equal to the number of occurences of ``A()`` in the degraded
    species. Thus, ``A(a=1) % A(a=1)`` would degrade twice as fast
    as ``A(a=None)`` under the above rule. If this behavior is not desired,
    the multiplicity can be fixed at one using the ``MatchOnce`` keyword:

    >>> Rule('A_deg', MatchOnce(A()) >> None, kdeg)     # doctest: +SKIP

    """
    cp = as_complex_pattern(pattern).copy()
    cp.match_once = True

```
