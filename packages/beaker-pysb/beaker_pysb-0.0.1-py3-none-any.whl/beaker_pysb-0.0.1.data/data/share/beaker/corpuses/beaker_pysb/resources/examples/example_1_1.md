# Description
This example demonstrates how to perform simulated annealing to minimize a function using different annealing schedules (cauchy, fast, and boltzmann).

# Code
```
import numpy as np
from numpy.random import uniform, normal

class base_schedule(object):
    def __init__(self):
        self.dwell = 20
        self.learn_rate = 0.5
        self.lower = -10
        self.upper = 10
        self.Ninit = 50
        self.accepted = 0
        self.tests = 0
        self.feval = 0
        self.k = 0
        self.T = None
        self.cvar = .05
    def init(self, **options):
        self.__dict__.update(options)
        self.lower = np.asarray(self.lower)
        self.lower = np.where(self.lower == np.NINF, np.finfo(float).min, self.lower)
        self.upper = np.asarray(self.upper)
        self.upper = np.where(self.upper == np.PINF, np.finfo(float).max, self.upper)
        self.k = 0
        self.accepted = 0
        self.feval = 0
        self.tests = 0
    def getstart_temp(self, best_state):
        print("Finding initial temperature")
        x0 = best_state.x
        for _ in range(self.Ninit):
            samp = np.squeeze(uniform(0, 1, size=self.dims)) - 0.5
            samp = samp / 0.5
            varx0 = x0 * samp * self.cvar
            x0 = x0 + varx0
            fval = self.func(x0, *self.args)
            self.feval += 1
            best_state.cost = min(fval, best_state.cost)
            if best_state.cost == fval:
                best_state.x = np.array(x0)
        self.T0 = (np.max(fval) - np.min(fval)) * 1.5
        return best_state.x
    def accept_test(self, dE):
        if dE < 0:
            self.accepted += 1
            return 1
        p = np.exp(-dE / self.boltzmann / self.T)
        if p > np.random.uniform(0.0, 1.0):
            self.accepted += 1
            return 1
        return 0

class fast_sa(base_schedule):
    def init(self, **options):
        super().init(**options)
        self.c = self.m * np.exp(-self.n * self.quench)
    def update_guess(self, x0):
        u = np.squeeze(uniform(0.0, 1.0, size=self.dims))
        T = self.T
        y = np.sign(u-0.5)*T*((1+1.0/T)**np.abs(2*u-1)-1.0)
        xc = y*(self.upper - self.lower)
        xnew = x0 + xc
        return xnew
    def update_temp(self):
        self.T = self.T0*np.exp(-self.c * self.k**(self.quench))
        self.k += 1

class cauchy_sa(base_schedule):
    def update_guess(self, x0):
        x0 = np.asarray(x0)
        numbers = np.squeeze(uniform(-np.pi/2, np.pi/2, size=self.dims))
        xc = self.learn_rate * self.T * np.tan(numbers)
        xnew = x0 + xc
        return xnew
    def update_temp(self):
        self.T = self.T0/(1+self.k)
        self.k += 1

class boltzmann_sa(base_schedule):
    def update_guess(self, x0):
        std = np.minimum(np.sqrt(self.T)*np.ones(self.dims), (self.upper-self.lower)/3.0/self.learn_rate)
        xc = np.squeeze(normal(0, 1.0, size=self.dims))
        xnew = x0 + xc*std*self.learn_rate
        return xnew
    def update_temp(self):
        self.k += 1
        self.T = self.T0 / np.log(self.k+1.0)

class _state(object):
    def __init__(self):
        self.x = None
        self.cost = None

def anneal(func, x0, args=(), schedule='fast', full_output=0, T0=None, Tf=1e-12, maxeval=None, maxaccept=None, maxiter=400, boltzmann=1.0, learn_rate=0.5, feps=1e-6, quench=1.0, m=1.0, n=1.0, lower=-100, upper=100, dwell=50, cvar=0.05):
    x0 = np.asarray(x0)
    lower = np.asarray(lower)
    upper = np.asarray(upper)
    schedule = eval(schedule+'_sa()')
    schedule.init(dims=np.shape(x0), func=func, args=args, boltzmann=boltzmann, T0=T0, learn_rate=learn_rate, lower=lower, upper=upper, m=m, n=n, quench=quench, dwell=dwell, cvar=cvar)
    current_state, last_state, best_state = _state(), _state(), _state()
    if T0 is None:
        best_state.x = x0
        x0 = schedule.getstart_temp(best_state)
    else:
        best_state.cost = float('inf')
    last_state.x = np.asarray(x0).copy()
    last_state.cost = func(x0, *args)
    schedule.feval += 1
    if last_state.cost < best_state.cost:
        best_state.cost = last_state.cost
        best_state.x = np.asarray(x0).copy()
    schedule.T = schedule.T0
    fqueue = [float('inf')] * 4
    iters = 0
    while True:
        for _ in range(dwell):
            current_state.x = schedule.update_guess(last_state.x)
            current_state.cost = func(current_state.x, *args)
            schedule.feval += 1
            dE = current_state.cost - last_state.cost
            if schedule.accept_test(dE):
                last_state.x = current_state.x.copy()
                last_state.cost = current_state.cost
                if last_state.cost < best_state.cost:
                    best_state.x = last_state.x.copy()
                    best_state.cost = last_state.cost
        schedule.update_temp()
        iters += 1
        fqueue.append(last_state.cost)
        fqueue.pop(0)
        if np.all(np.abs((np.array(fqueue) - fqueue[0]) / fqueue[0]) < feps):
            retval = 0
            break
        elif (Tf is not None) and (schedule.T < Tf):
            retval = 1
            break
        elif (maxeval is not None) and (schedule.feval > maxeval):
            retval = 2
            break
        elif (iters > maxiter):
            retval = 3
            break
        elif (maxaccept is not None) and (schedule.accepted > maxaccept):
            retval = 4
            break
    if full_output:
        return best_state.x, best_state.cost, schedule.T, schedule.feval, iters, schedule.accepted, retval
    else:

if __name__ == "__main__":
    from numpy import cos
    # minimum expected at ~-0.195
    func = lambda x: cos(14.5*x-0.3) + (x+0.2)*x
    print(anneal(func,1.0,full_output=1,upper=3.0,lower=-3.0,feps=1e-4,maxiter=2000,schedule='cauchy'))
    print(anneal(func,1.0,full_output=1,upper=3.0,lower=-3.0,feps=1e-4,maxiter=2000,schedule='fast'))
    print(anneal(func,1.0,full_output=1,upper=3.0,lower=-3.0,feps=1e-4,maxiter=2000,schedule='boltzmann'))

    # minimum expected at ~[-0.195, -0.1]
    func = lambda x: cos(14.5*x[0]-0.3) + (x[1]+0.2)*x[1] + (x[0]+0.2)*x[0]
    print(anneal(func,[1.0, 1.0],full_output=1,upper=[3.0, 3.0],lower=[-3.0, -3.0],feps=1e-4,maxiter=2000,schedule='cauchy'))
    print(anneal(func,[1.0, 1.0],full_output=1,upper=[3.0, 3.0],lower=[-3.0, -3.0],feps=1e-4,maxiter=2000,schedule='fast'))

```
