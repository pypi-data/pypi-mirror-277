# Description
Export a PySB model to SBML format interactively

# Code
```
from pysb.examples.robertson import model

    sbml_output = export(model, 'sbml')

The output (a string) can be inspected or written to a file, e.g. as follows::

    with open('robertson.sbml', 'w') as f:

```
