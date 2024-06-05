# Description
Load parameter values from a CSV file into a dictionary.

# Code
```

def load_params(fname):
    """load the parameter values from a csv file, return them as dict.
    """
    parmsff = {}
    # FIXME: This might fail if a parameter name is larger than 50 characters.
    # FIXME: Maybe do this with the csv module instead?
    temparr = numpy.loadtxt(fname, dtype=([('a','S50'),('b','f8')]), delimiter=',') 
    for i in temparr:
        parmsff[i[0]] = i[1]

```
