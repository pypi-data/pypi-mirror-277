# Description
Sensitivity analysis on the Tyson cell cycle model using the PairwiseSensitivity class.

# Code
```
import numpy as np
from pysb.simulator.scipyode import ScipyOdeSimulator

>>> from pysb.examples.tyson_oscillator import model
>>> import numpy as np
>>> from pysb.simulator.scipyode import ScipyOdeSimulator
>>> np.set_printoptions(precision=4, suppress=True)
>>> tspan=np.linspace(0, 200, 201)
>>> observable = 'Y3'
>>> values_to_sample = [.8, 1.2]
>>> def obj_func_cell_cycle(out):
...     timestep = tspan[:-1]
...     y = out[:-1] - out[1:]
...     freq = 0
...     local_times = []
...     prev = y[0]
...     for n in range(1, len(y)):
...         if y[n] > 0 > prev:
...             local_times.append(timestep[n])
...             freq += 1
...         prev = y[n]
...     local_times = np.array(local_times)
...     local_freq = np.average(local_times)/len(local_times)*2
...     return local_freq
>>> solver = ScipyOdeSimulator(model, tspan, integrator='lsoda',\
                  integrator_options={'atol' : 1e-8,\
                                      'rtol' : 1e-8,\
                                      'mxstep' :20000})
>>> sens = PairwiseSensitivity(\
        values_to_sample=values_to_sample,\
        observable=observable,\
        objective_function=obj_func_cell_cycle,\
        solver=solver\
    )
>>> print(sens.b_matrix)
[[((0.8, 'cdc0'), (0.8, 'cdc0')) ((0.8, 'cdc0'), (1.2, 'cdc0'))
  ((0.8, 'cdc0'), (0.8, 'cyc0')) ((0.8, 'cdc0'), (1.2, 'cyc0'))]
 [((1.2, 'cdc0'), (0.8, 'cdc0')) ((1.2, 'cdc0'), (1.2, 'cdc0'))
  ((1.2, 'cdc0'), (0.8, 'cyc0')) ((1.2, 'cdc0'), (1.2, 'cyc0'))]
 [((0.8, 'cyc0'), (0.8, 'cdc0')) ((0.8, 'cyc0'), (1.2, 'cdc0'))
  ((0.8, 'cyc0'), (0.8, 'cyc0')) ((0.8, 'cyc0'), (1.2, 'cyc0'))]
 [((1.2, 'cyc0'), (0.8, 'cdc0')) ((1.2, 'cyc0'), (1.2, 'cdc0'))
  ((1.2, 'cyc0'), (0.8, 'cyc0')) ((1.2, 'cyc0'), (1.2, 'cyc0'))]]
>>> sens.run()
>>> print(sens.p_matrix)#doctest: +NORMALIZE_WHITESPACE
[[ 0.      0.      5.0243 -4.5381]
 [ 0.      0.      5.0243 -4.5381]
 [ 5.0243  5.0243  0.      0.    ]
 [-4.5381 -4.5381  0.      0.    ]]
>>> print(sens.p_prime_matrix) #doctest: +NORMALIZE_WHITESPACE
 [[ 0.      0.      5.0243 -4.5381]
  [ 0.      0.      5.0243 -4.5381]
  [ 0.      0.      0.      0.    ]
  [ 0.      0.      0.      0.    ]]
>>> print(sens.p_matrix - sens.p_prime_matrix) \
        #doctest: +NORMALIZE_WHITESPACE
 [[ 0.      0.      0.      0.    ]
  [ 0.      0.      0.      0.    ]
  [ 5.0243  5.0243  0.      0.    ]
  [-4.5381 -4.5381  0.      0.    ]]
>>> sens.create_boxplot_and_heatplot() #doctest: +SKIP
>>> values_to_sample = [.9, 1.1]
>>> sens = PairwiseSensitivity(\
        values_to_sample=values_to_sample,\
        observable=observable,\
        objective_function=obj_func_cell_cycle,\
        solver=solver,\
        sens_type='params'\
    )
>>> print(sens.b_matrix.shape == (14, 14))
True
>>> sens.run()
>>> print(sens.p_matrix)#doctest: +NORMALIZE_WHITESPACE
[[  0.       0.      13.6596  13.6596  24.3955   4.7909  16.4603  11.3258
    0.1621  31.2804  13.6596  13.6596  13.6596  13.6596]
 [  0.       0.     -10.3728 -10.3728  -3.7277 -14.9803  -7.2934 -12.2416
  -18.3144   0.     -10.3728 -10.3728 -10.3728 -10.3728]
 [ 13.6596 -10.3728   0.       0.       7.3582  -6.483    3.0794  -2.269
  -10.6969  12.7261   0.       0.       0.       0.    ]
 [ 13.6596 -10.3728   0.       0.       7.3582  -6.483    3.0794  -2.269
  -10.6969  12.7261   0.       0.       0.       0.    ]
 [ 24.3955  -3.7277   7.3582   7.3582   0.       0.      10.859    5.2577
   -4.376   23.2285   7.3582   7.3582   7.3582   7.3582]
 [  4.7909 -14.9803  -6.483   -6.483    0.       0.      -3.4036  -9.0762
  -15.2185   3.8574  -6.483   -6.483   -6.483   -6.483 ]
 [ 16.4603  -7.2934   3.0794   3.0794  10.859   -3.4036   0.       0.
   -7.9417  15.5267   3.0794   3.0794   3.0794   3.0794]
 [ 11.3258 -12.2416  -2.269   -2.269    5.2577  -9.0762   0.       0.
  -13.128   10.859   -2.269   -2.269   -2.269   -2.269 ]
 [  0.1621 -18.3144 -10.6969 -10.6969  -4.376  -15.2185  -7.9417 -13.128
    0.       0.     -10.6969 -10.6969 -10.6969 -10.6969]
 [ 31.2804   0.      12.7261  12.7261  23.2285   3.8574  15.5267  10.859
    0.       0.      12.7261  12.7261  12.7261  12.7261]
 [ 13.6596 -10.3728   0.       0.       7.3582  -6.483    3.0794  -2.269
  -10.6969  12.7261   0.       0.       0.       0.    ]
 [ 13.6596 -10.3728   0.       0.       7.3582  -6.483    3.0794  -2.269
  -10.6969  12.7261   0.       0.       0.       0.    ]
 [ 13.6596 -10.3728   0.       0.       7.3582  -6.483    3.0794  -2.269
  -10.6969  12.7261   0.       0.       0.       0.    ]
 [ 13.6596 -10.3728   0.       0.       7.3582  -6.483    3.0794  -2.269
  -10.6969  12.7261   0.       0.       0.       0.    ]]
>>> print(sens.p_matrix - sens.p_prime_matrix) \
        #doctest: +NORMALIZE_WHITESPACE
 [[  0.       0.      13.6596  13.6596  17.0373  11.2739  13.3809  13.5948
   10.859   18.5543  13.6596  13.6596  13.6596  13.6596]
 [  0.       0.     -10.3728 -10.3728 -11.0859  -8.4973 -10.3728  -9.9725
   -7.6175 -12.7261 -10.3728 -10.3728 -10.3728 -10.3728]
 [  0.       0.       0.       0.       0.       0.       0.       0.
    0.       0.       0.       0.       0.       0.    ]
 [  0.       0.       0.       0.       0.       0.       0.       0.
    0.       0.       0.       0.       0.       0.    ]
 [ 10.7358   6.6451   7.3582   7.3582   0.       0.       7.7796   7.5267
    6.3209  10.5024   7.3582   7.3582   7.3582   7.3582]
 [ -8.8687  -4.6075  -6.483   -6.483    0.       0.      -6.483   -6.8071
   -4.5215  -8.8687  -6.483   -6.483   -6.483   -6.483 ]
 [  2.8006   3.0794   3.0794   3.0794   3.5008   3.0794   0.       0.
    2.7553   2.8006   3.0794   3.0794   3.0794   3.0794]
 [ -2.3339  -1.8688  -2.269   -2.269   -2.1005  -2.5932   0.       0.
   -2.4311  -1.8671  -2.269   -2.269   -2.269   -2.269 ]
 [-13.4976  -7.9417 -10.6969 -10.6969 -11.7342  -8.7355 -11.0211 -10.859
    0.       0.     -10.6969 -10.6969 -10.6969 -10.6969]
 [ 17.6207  10.3728  12.7261  12.7261  15.8703  10.3404  12.4473  13.128
    0.       0.      12.7261  12.7261  12.7261  12.7261]
 [  0.       0.       0.       0.       0.       0.       0.       0.
    0.       0.       0.       0.       0.       0.    ]
 [  0.       0.       0.       0.       0.       0.       0.       0.
    0.       0.       0.       0.       0.       0.    ]
 [  0.       0.       0.       0.       0.       0.       0.       0.
    0.       0.       0.       0.       0.       0.    ]
 [  0.       0.       0.       0.       0.       0.       0.       0.
    0.       0.       0.       0.       0.       0.    ]]

```
