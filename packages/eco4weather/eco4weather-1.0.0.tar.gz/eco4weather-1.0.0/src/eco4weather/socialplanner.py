"""
Author : Olivier Pannekoucke
Creation Date :  2024-03-26 
Modifications : None
"""

import sympkf
import numpy as np
import scipy.optimize as opt

class SocialPlanner(sympkf.Model):
    '''
    Computation of the optimal path provided by a Social Planner that maximizes the social welfare
    
    In this implementation the optimization relies on an optimizer that minimizes a function.
    Hence, the `objective function` is defined as the opposite of the social welfare.
    '''
    
    def __init__(self, *args, nbyears=100, dt=0.5, time_scheme='euler', name='Abstract Social Planner', **kwargs):
        super().__init__(*args, time_scheme=time_scheme, **kwargs)
        self.nbyears = nbyears
        self._dt = dt
        self._time_window = self.window(nbyears)
        self._ndt = len(self._time_window)
        dt = self._time_window[1]
        self._opt_control = None
        self._opt_traj = None
        self._name = name
        print(f'Time scheme is {time_scheme.title()} for Econ studies, with time step dt of {dt} yr, over {self.nbyears} years')
        
        
    @property
    def name(self):
        return self._name
    
    @property
    def time_window(self):
        return self._time_window            
    
    @property
    def ndt(self):
        return self._ndt
        
    def control(self, t):
        idx = np.argmin( np.abs(self.time_window-t) )
        return self.__control[idx]
    
    def trend(self, t, state):
        raise NotImplementedError
        
    def set_control(self, control):
        self.__control = control    
    
    def predict(self, state0, control):
        self.set_control(control)
        return super().predict(self.time_window, state0)
            
    def societal_utility(self, control, traj):
        raise NotImplementedError
        
    def welfare(self, control, state0 ):
        '''
        Welfare function which is a weighted sum of the societal utilities over a time window
        '''                                
        traj = self.predict(state0, control)
        return np.sum( self.societal_utility(control,traj))

    def objfunc(self, control, state0):
        """        
        Objective function for optimization of the welfare
        Note that position of control and state0 is mandatory when using optimize toolbox, and should not be switched.
        """        
        return -self.welfare(control, state0) # Minimisation de l'opposée du bien être sociétal pour le maximiser.
                
    def optimize(self, state0, bound=1., initial_control=None):
        """
        bound =1. for $c$ means that the consumption can not be larger than the GDP (no direct consumption of the capital).
        However, this could be modified.
        """
        initial_control = 0*self.time_window if initial_control is None else initial_control
        bounds = [(0., bound) for t in range(self.ndt)] # Bounds for the extraction. 
        opt_control = opt.minimize(self.objfunc, initial_control, 
                             args=(state0,),  # Additionnal arguments to provide to the objective function
                             bounds = tuple(bounds), # Bounds for seeking the consumption rate that ranges within [0,1]
                             method='SLSQP', options={'disp': True})
        self._opt_control = np.copy(opt_control.x)
        self._opt_traj = self.predict(state0, self._opt_control)

    @property
    def opt_traj(self):
        return self._opt_traj
    
    @property
    def opt_control(self):
        return self._opt_control