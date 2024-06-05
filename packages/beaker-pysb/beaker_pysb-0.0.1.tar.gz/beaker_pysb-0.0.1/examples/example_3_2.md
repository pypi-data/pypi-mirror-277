# Description
This example demonstrates defining and using MultiState for Monomers to model molecules with multiple sites that may be identical. It explains how to set up Monomers with duplicate sites and showcases specific patterns.

# Code
```
import sympy
import networkx as nx
from collections.abc import Iterable

class Component:
    pass

class Model:
    pass

def validate_site_value(state, monomer=None, site=None, _in_multistate=False):
    return True

class MultiState(object):
    def __init__(self, *args):
        if len(args) == 1:
            raise ValueError('MultiState should not be used when only a single site is specified')
        self.sites = args
        for s in self.sites:
            validate_site_value(s, _in_multistate=True)

    def __len__(self):
        return len(self.sites)

    def __iter__(self):
        return iter(self.sites)

    def __repr__(self):

    When declared, a MultiState instance is not connected to any Monomer or
    site, so full validation is deferred until it is used as part of a
    :py:class:`MonomerPattern` or :py:class:`ComplexPattern`.

    Examples
    --------

    Define a Monomer "A" with MultiState "a", which has two copies, and
    Monomer "B" with MultiState "b", which also has two copies but can take
    state values "u" and "p":

    >>> Model()  # doctest:+ELLIPSIS
    <Model '_interactive_' (monomers: 0, ...
    >>> Monomer('A', ['a', 'a'])  # BNG: A(a, a)
    Monomer('A', ['a', 'a'])
    >>> Monomer('B', ['b', 'b'], {'b': ['u', 'p']})  # BNG: B(b~u~p, b~u~p)
    Monomer('B', ['b', 'b'], {'b': ['u', 'p']})

    To specify MultiStates, use the MultiState class. Here are some valid
    examples of MultiState patterns, with their BioNetGen equivalents:

    >>> A(a=MultiState(1, 2))  # BNG: A(a!1,a!2)
    A(a=MultiState(1, 2))
    >>> B(b=MultiState('u', 'p'))  # BNG: A(A~u,A~p)
    B(b=MultiState('u', 'p'))
    >>> A(a=MultiState(1, 2)) % B(b=MultiState(('u', 1), 2))  # BNG: A(a!1, a!2).B(b~u!1, b~2)

```
