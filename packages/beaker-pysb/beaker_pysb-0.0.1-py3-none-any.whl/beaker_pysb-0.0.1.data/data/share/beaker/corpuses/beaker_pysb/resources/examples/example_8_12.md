# Description
Generate a reaction which degrades a species using degrade function.

# Code
```

    Degrade all B, even bound species::

        Model()
        Monomer('B', ['x'])
        degrade(B(), 1e-6)

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> Monomer('B', ['x'])
        Monomer('B', ['x'])
        >>> degrade(B(), 1e-6) # doctest:+NORMALIZE_WHITESPACE
        ComponentSet([
         Rule('degrade_B', B() >> None, degrade_B_k),
         Parameter('degrade_B_k', 1e-06),

```
