# Description
Generate rules to bind a monomer to a circular homomeric pore using pore_bind function.

# Code
```

    Specify that a cargo molecule can bind reversibly to a 3-membered
    pore::

        Model()
        Monomer('Unit', ['p1', 'p2', 'sc_site'])
        Monomer('Cargo', ['c_site'])
        pore_bind(Unit, 'p1', 'p2', 'sc_site', 3, 
                  Cargo(), 'c_site', [1e-4, 1e-1, 1])

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('Unit', ['p1', 'p2', 'sc_site'])
        Monomer('Unit', ['p1', 'p2', 'sc_site'])
        >>> Monomer('Cargo', ['c_site'])
        Monomer('Cargo', ['c_site'])
        >>> pore_bind(Unit, 'p1', 'p2', 'sc_site', 3, 
        ...           Cargo(), 'c_site', [1e-4, 1e-1, 1]) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('pore_bind_Unit_3_Cargo',
             MatchOnce(Unit(p1=3, p2=1, sc_site=None) %
                 Unit(p1=1, p2=2, sc_site=None) %
                 Unit(p1=2, p2=3, sc_site=None)) +
                 Cargo(c_site=None) |
             MatchOnce(Unit(p1=3, p2=1, sc_site=4) %
                 Unit(p1=1, p2=2, sc_site=None) %
                 Unit(p1=2, p2=3, sc_site=None) %
                 Cargo(c_site=4)),
             pore_bind_Unit_3_Cargo_kf, pore_bind_Unit_3_Cargo_kr),
         Parameter('pore_bind_Unit_3_Cargo_kf', 0.0001),
         Parameter('pore_bind_Unit_3_Cargo_kr', 0.1),

```
