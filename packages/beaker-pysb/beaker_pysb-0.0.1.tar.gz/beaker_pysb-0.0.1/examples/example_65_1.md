# Description
Run EARM and Robertson example models from PySB and compare runtimes with and without inline compilation and analytically-derived Jacobian.

# Code
```
import timeit
from pysb.integrate import Solver
from pysb.examples import robertson, earm_1_0

if __name__ == '__main__':
    arg_list = [(0, 0), (0, 1), (1, 0), (1, 1)]

    print("-- EARM --")
    earm_tspan = np.linspace(0, 1e4, 1000)
    for args in arg_list:
        check_runtime(earm_1_0.model, earm_tspan, 1000, *args)

    print("-- Robertson --")
    rob_tspan = np.linspace(0, 100)
    for args in arg_list:

```
