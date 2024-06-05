# Description
Check the components of a Model against a provided list of components

# Code
```

def check_model_against_component_list(model, component_list):
    """Check the components of the given model against the provided list
    of components, asserting that they are equal. Useful for testing a
    model against a previously validated (and serialized) state.

    Currently checks equality by performing a string comparison of the
    repr() of each component, however, this may be revised to use alternative
    measures of equality in the future.
    
    To serialize the list of components to create a record of a
    validated state, see :py:func:`serialize_component_list`.
    """
    assert len(model.all_components()) == len(component_list), \
           "Model %s does not have the same " \
           "number of components as the previously validated version. " \
           "The validated model has %d components, current model has " \
           "%d components." % \
           (model.name, len(model.all_components()), len(component_list))

    model_components = list(model.all_components().values())
    for i, comp in enumerate(component_list):
        model_comp_str = repr(model_components[i])
        comp_str = repr(comp) 
        assert comp_str == model_comp_str, \
               "Model %s does not match reference version: " \
               "Mismatch at component %d: %s in the reference model not " \
               "equal to %s in the current model." \
                % (model.name, i, comp_str, model_comp_str)


```
