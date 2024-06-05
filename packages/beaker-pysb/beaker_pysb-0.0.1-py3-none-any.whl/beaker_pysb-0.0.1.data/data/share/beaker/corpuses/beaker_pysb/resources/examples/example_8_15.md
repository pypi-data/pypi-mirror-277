# Description
Generate rules to transport cargo through a circular homomeric pore using pore_transport function.

# Code
```

    Specify that a three-membered pore is capable of
    transporting cargo from the mitochondria to the cytoplasm::

        Model()
        Monomer('Unit', ['p1', 'p2', 'sc_site'])
        Monomer('Cargo', ['c_site', 'loc'], {'loc':['mito', 'cyto']})
        pore_transport(Unit, 'p1', 'p2', 'sc_site', 3, 3,
                       Cargo(loc='mito'), 'c_site', Cargo(loc='cyto'),
                       [[1e-4, 1e-1, 1]])

    Generates two rules--one (reversible) binding rule and one transport
    rule--and the three associated parameters.

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('Unit', ['p1', 'p2', 'sc_site'])
        Monomer('Unit', ['p1', 'p2', 'sc_site'])
        >>> Monomer('Cargo', ['c_site', 'loc'], {'loc':['mito', 'cyto']})
        Monomer('Cargo', ['c_site', 'loc'], {'loc': ['mito', 'cyto']})
        >>> pore_transport(Unit, 'p1', 'p2', 'sc_site', 3, 3,
        ...                Cargo(loc='mito'), 'c_site', Cargo(loc='cyto'),
        ...                [[1e-4, 1e-1, 1]]) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('pore_transport_complex_Unit_3_Cargomito',
             MatchOnce(Unit(p1=3, p2=1, sc_site=None) %
                 Unit(p1=1, p2=2, sc_site=None) %
                 Unit(p1=2, p2=3, sc_site=None)) +
                 Cargo(c_site=None, loc='mito') |
             MatchOnce(Unit(p1=3, p2=1, sc_site=4) %
                 Unit(p1=1, p2=2, sc_site=None) %
                 Unit(p1=2, p2=3, sc_site=None) %
                 Cargo(c_site=4, loc='mito')),
             pore_transport_complex_Unit_3_Cargomito_kf,
             pore_transport_complex_Unit_3_Cargomito_kr),
         Parameter('pore_transport_complex_Unit_3_Cargomito_kf', 0.0001),
         Parameter('pore_transport_complex_Unit_3_Cargomito_kr', 0.1),
         Rule('pore_transport_dissociate_Unit_3_Cargocyto',
             MatchOnce(Unit(p1=3, p2=1, sc_site=4) %
                 Unit(p1=1, p2=2, sc_site=None) %
                 Unit(p1=2, p2=3, sc_site=None) %
                 Cargo(c_site=4, loc='mito')) >>
             MatchOnce(Unit(p1=3, p2=1, sc_site=None) %
                 Unit(p1=1, p2=2, sc_site=None) %
                 Unit(p1=2, p2=3, sc_site=None)) +
                 Cargo(c_site=None, loc='cyto'),
             pore_transport_dissociate_Unit_3_Cargocyto_kc),
         Parameter('pore_transport_dissociate_Unit_3_Cargocyto_kc', 1.0),

```
