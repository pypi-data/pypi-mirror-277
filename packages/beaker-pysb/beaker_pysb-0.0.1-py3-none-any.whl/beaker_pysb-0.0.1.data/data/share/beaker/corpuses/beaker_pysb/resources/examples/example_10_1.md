# Description
Serialize (pickle) the components of a Model to a file

# Code
```
from pysb.core import Model

def serialize_component_list(model, filename):
    """Serialize (pickle) the components of the given model to a file. This can
    later be used to compare the state of the model against a previously
    validated state using :py:func:`check_model_against_component_list`.
    """

    f = open(filename, 'w')
    pickle.dump(list(model.all_components().values()), f)

```
