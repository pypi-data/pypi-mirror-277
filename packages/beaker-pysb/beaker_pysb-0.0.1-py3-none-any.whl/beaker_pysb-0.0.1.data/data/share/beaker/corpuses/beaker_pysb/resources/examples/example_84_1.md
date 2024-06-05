# Description
Testing the alias_model_components() function from pysb.util to ensure it exports components to the global namespace.

# Code
```
from pysb.core import Model, Monomer

def test_alias_model_components():
    """
    Tests that alias_model_components() exports to the global namespace
    """
    m = Model(_export=False)
    m.add_component(Monomer('A', _export=False))
    assert 'A' not in globals()
    alias_model_components(m)

    # A should now be defined in the namespace - try deleting it
    assert isinstance(globals()['A'], Monomer)

    # Delete the monomer to cleanup the global namespace

```
