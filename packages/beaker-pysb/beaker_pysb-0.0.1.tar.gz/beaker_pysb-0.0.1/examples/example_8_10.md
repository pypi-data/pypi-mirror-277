# Description
Create fwd and reverse rules for catalysis of the form E + S -> E + P, P -> S using catalyze_one_step_reversible function.

# Code
```

    --------
    One-step, pseudo-first order conversion of S to P by E::

        Model()
        Monomer('E', ['b'])
        Monomer('S', ['b'])
        Monomer('P')
        catalyze_one_step_reversible(E, S, P, [1e-1, 1e-4])

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('E', ['b'])
        Monomer('E', ['b'])
        >>> Monomer('S', ['b'])
        Monomer('S', ['b'])
        >>> Monomer('P')
        Monomer('P')
        >>> catalyze_one_step_reversible(E, S, P, [1e-1, 1e-4]) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('one_step_E_S_to_E_P', E() + S() >> E() + P(), one_step_E_S_to_E_P_kf),
         Parameter('one_step_E_S_to_E_P_kf', 0.1),
         Rule('reverse_P_to_S', P() >> S(), reverse_P_to_S_kr),
         Parameter('reverse_P_to_S_kr', 0.0001),

```
