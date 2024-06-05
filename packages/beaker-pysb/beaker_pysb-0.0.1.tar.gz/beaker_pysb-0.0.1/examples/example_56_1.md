# Description
Create a PySB Model based on a BioModels SBML model, then print the model's summary.

# Code
```

from pysb.importers.sbml import model_from_biomodels
model = model_from_biomodels('1')           #doctest: +SKIP
print(model)                                #doctest: +SKIP

```
