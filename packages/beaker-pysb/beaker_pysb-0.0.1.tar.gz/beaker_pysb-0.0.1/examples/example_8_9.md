# Description
Generate the one-step catalytic reaction E + S >> E + P using catalyze_one_step function.

# Code
```

    Convert S to P by E::

        Model()
        Monomer('E', ['b'])
        Monomer('S', ['b'])
        Monomer('P')
        catalyze_one_step(E, S, P, 1e-4)

    If the ability of the enzyme E to catalyze this reaction is dependent
    on the site 'b' of E being unbound, then this macro must be called as

        catalyze_one_step(E(b=None), S, P, 1e-4)

    and similarly if the substrate or product must be unbound.

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('E', ['b'])
        Monomer('E', ['b'])
        >>> Monomer('S', ['b'])
        Monomer('S', ['b'])
        >>> Monomer('P')
        Monomer('P')
        >>> catalyze_one_step(E, S, P, 1e-4) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('one_step_E_S_to_E_P', E() + S() >> E() + P(), one_step_E_S_to_E_P_kf),
         Parameter('one_step_E_S_to_E_P_kf', 0.0001),

```
