# Description
Running a simulation using the OpenCLSSA simulator

# Code
```
import numpy as np
from pysb.simulator.base import SimulationResult
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import pyopencl as cl
from pyopencl import array as ocl_array
import time

class OpenCLSSASimulator(SSABase):
    def __init__(self, model, verbose=False, tspan=None, precision=np.float64, **kwargs):
        if cl is None:
            raise ImportError('pyopencl library required for {}'> ''.format(self.__class__.__name__))
        super(OpenCLSSASimulator, self).__init__(model, verbose, **kwargs)
        generate_equations(self._model)
        self.tspan = tspan
        self.verbose = verbose
        self._step_0 = True
        self._dtype = precision
        template_code = Template(filename=os.path.join(os.path.dirname(__file__), 'templates', 'opencl_ssa.cl'))
        args = self._get_template_args()
        if self._dtype == np.float32:
            args['prec'] = '#define USE_SINGLE_PRECISION'
            self._logger.warn("Should be cautious using single precision.")
        else:
            args['prec'] = '#define USE_DOUBLE_PRECISION'
        _d = {np.uint32: "uint", np.int32: 'int', np.int16: 'ushort', np.int64: 'long', np.uint64: 'unsigned long'}
        self._dtype_species = np.int32
        args['spc_type'] = _d[self._dtype_species]
        if verbose == 2:
            args['verbose'] = '#define VERBOSE'
        elif verbose > 3:
            args['verbose'] = '#define VERBOSE_MAX'
        else:
            args['verbose'] = ''
        self._logger.info("Initialized OpenCLSSASimulator class")

    def run(self, tspan=None, param_values=None, initials=None, number_sim=0,
            random_seed=0):
        """
        Run a simulation and returns the result (trajectories)

        .. note::
            In early versions of the Simulator class, ``tspan``, ``initials``
            and ``param_values`` supplied to this method persisted to future
            :func:`run` calls. This is no longer the case.

        Parameters
        ----------
        tspan
        initials
        param_values
            See parameter definitions in :class:`ScipyOdeSimulator`.
        number_sim: int
            Number of simulations to perform
        random_seed: int
            Seed used for random numbers to be passed to device.

        Returns
        -------
        A :class:`SimulationResult` object
        """
        super(OpenCLSSASimulator, self).run(tspan=tspan, initials=initials,
                                            param_values=param_values,
                                            number_sim=number_sim)
        if tspan is None:
            if self.tspan is None:
                raise Exception("Please provide tspan")
            else:
                tspan = self.tspan
        # tspan for each simulation
        t_out = np.array(tspan, dtype=self._dtype)
        # compile kernel and send parameters to GPU
        if self._step_0:
            self._setup()

        self._logger.info("Creating content on device")
        # If there is more than one device, split number of simulations
        # over all devices equally
        n_sim_per_device = self.num_sim//self._n_devices

        local_work_size = self._local_work_size
        # Number of blocks refers to how many warps/wavefronts to be run
        # at the same time. Threads is how many simulations per warp/wavefront
        # Number together will be equal to total number of simulations, or
        # the next number of blocks up
        # (100 simulations, 32 threads/block, 4 blocks)
        # Ideally one would run a multiple of local_work_size[0]
        blocks, threads = self.get_blocks(n_sim_per_device,
                                          local_work_size[0])

        total_threads = int(blocks * threads)

        # retrieve and store results
        timer_start = time.time()

        # allows multiple GPUs to be used
        with ThreadPoolExecutor(self._n_devices) as executor:
            sim_partial = partial(call, ocl_instance=self,
                                  n_sim_per_device=n_sim_per_device,
                                  t_out=t_out,
                                  total_threads=total_threads,
                                  local_work_size=local_work_size,
                                  random_seed=random_seed)
            results = [executor.submit(sim_partial, i)
                       for i in range(self._n_devices)]
            traj = [r.result() for r in results]
        traj = [r.reshape((total_threads, len(t_out), self._n_species))
                for r in traj]
        traj = np.vstack(traj)
        traj = traj[:self.num_sim]
        self._time = time.time() - timer_start
        self._logger.info("{} simulations "
                          "in {:.4f}s".format(self.num_sim, self._time))

        tout = np.array([tspan] * self.num_sim)

```
