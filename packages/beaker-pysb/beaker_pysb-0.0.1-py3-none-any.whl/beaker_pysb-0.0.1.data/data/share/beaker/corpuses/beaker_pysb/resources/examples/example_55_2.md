# Description
Create a PySB model from a JSON string.

# Code
```
import json
from pysb.builder import Builder
from pysb.core import RuleExpression, ReactionPattern, ComplexPattern, MonomerPattern, MultiState, ANY, WILD, Parameter, Expression
from pysb.annotation import Annotation
from pysb.pattern import SpeciesPatternMatcher
import sympy
import re
import warnings
from collections.abc import Mapping
from sympy.parsing.sympy_parser import parse_expr

class PySBJSONDecodeError(ValueError):
    pass

class PySBJSONDecoder(JSONDecoder):
    MAX_SUPPORTED_PROTOCOL = 2

def model_from_json(json_str):

```
