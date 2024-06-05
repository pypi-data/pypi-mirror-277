# Description
Generate a rule to simulate passing of time and create a time observable that can be used in complex Expression rates using create_t_obs function.

# Code
```

     Create rule to simulate passing of time and time observable::

        Model()
        create_t_obs()

    Execution::

        >>> Model() # doctest:+ELLIPSIS
        <Model '_interactive_' ...>
        >>> create_t_obs()
        ComponentSet([
         Rule('synthesize___t', None >> __t(), __k_t),
         Monomer('__t'),
         Parameter('__k_t', 1.0),
         Observable('t', __t()),

```
