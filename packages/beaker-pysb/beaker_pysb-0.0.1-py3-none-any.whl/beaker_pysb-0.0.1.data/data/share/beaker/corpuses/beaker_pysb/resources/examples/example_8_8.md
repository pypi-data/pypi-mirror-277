# Description
Generate the two-step catalytic reaction E + S | E:S >> E + P using catalyze function.

# Code
```

    Using distinct Monomers for substrate and product::

        Model()
        Monomer('E', ['b'])
        Monomer('S', ['b'])
        Monomer('P')
        catalyze(E(), 'b', S(), 'b', P(), (1e-4, 1e-1, 1))

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('E', ['b'])
        Monomer('E', ['b'])
        >>> Monomer('S', ['b'])
        Monomer('S', ['b'])
        >>> Monomer('P')
        Monomer('P')
        >>> catalyze(E(), 'b', S(), 'b', P(), (1e-4, 1e-1, 1)) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('bind_E_S_to_ES', E(b=None) + S(b=None) | E(b=1) % S(b=1),
             bind_E_S_to_ES_kf, bind_E_S_to_ES_kr),
         Parameter('bind_E_S_to_ES_kf', 0.0001),
         Parameter('bind_E_S_to_ES_kr', 0.1),
         Rule('catalyze_ES_to_E_P', E(b=1) % S(b=1) >> E(b=None) + P(),
             catalyze_ES_to_E_P_kc),
         Parameter('catalyze_ES_to_E_P_kc', 1.0),

```
