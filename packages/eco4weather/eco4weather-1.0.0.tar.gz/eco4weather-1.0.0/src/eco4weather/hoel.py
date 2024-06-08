"""
Author : Olivier Pannekoucke
Creation Date :  2024-03-26 
Modifications : None
"""
import numpy as np
from .socialplanner import SocialPlanner
import matplotlib.pyplot as plt

class SimplifiedHoelKverndokk(SocialPlanner):
    '''
    Simplified version of the Hoel and Kverndokk model where the social welfare is given
    as an utility `u(x)` function of the extraction and consumption of an exhaustible 
    ressource (fossil fuel) whose consumption realeases carbon in the atmosphere,
    minus a damage function `D(S)` where `S` denotes the atmospheric stock of carbon.
    This simplified version, is similar to Eq.(1) when there is no marginal cost of extraction 
    (the cumulative extraction is not considered). 
    The utility function is given as the CRRA 

    $$ u_γ(x) = x^{1-γ}/(1-γ) $$

    Here the damage function is defined as 

    $$ D(S) = ω S^2 $$
    
    References
    ---
    
    M. Hoel and S. Kverndokk, “Depletion of fossil fuels and the impacts of global warming,” 
    Resource and Energy Economics, vol. 18, no. 2, pp. 115–136, Jun. 1996, 
    doi: 10.1016/0928-7655(96)00005-x.
    
    '''
    
    def __init__(self, *args, nbyears=100, r=0.015, δ=0.1, γ=0.5, ω=0.033, **kwargs):        
        super().__init__(*args, **kwargs)  
        self.δ = δ  # Depreciation ..                         / δ = 0.1   /  
        self.r = r  # Discount rate for intertemporal utility / r = 0.015 / 
        self.γ = γ  # Relative Risk Aversion                  / γ = 0.5   /
        self.ω = ω  # Damage factor.                          / ω = 0.033 /
        
        # Discount rate (intertemporal discount rate)
        dt = self.time_window[1]
        self.β = np.exp(-r*dt)
        # Equilibrium when there is no extraction cost
        self.x_star = (2*self.ω / (self.δ*(self.r+self.δ)))**(-1/(1.+self.γ))
        self.S_star = self.x_star / self.δ 
                        
    def u(self, x):
        """
        utility of using fossil fuel
        """
        γ = self.γ
        if γ==1.:
            return np.log(x)
        else:
            return np.power(x,1.-γ)/(1.-γ)                
            
    def u_prime(self, x):
        h = 1e-7
        return np.imag(self.u(x+1j*h)/h)         
    
    def damage(self, S):        
        return self.ω*S**2
    
    def trend(self, t, state):
        S = state
        xt = self.control(t)
        dS = xt - self.δ*S
        return dS
    
    def societal_utility(self, control, traj):
        S = traj
        x = control        
        return (self.u(x)-self.damage(S) )*np.power(self.β,self.time_window)

    def plot_traj(self, equilirium_idx = None, control=None, traj=None):
        """
        Plot of the economical path in the reduced formulation of the HK model.
        When control and traj are None, the path is the optimal one
        """
        
        equilirium_idx = self.ndt//2 if equilirium_idx is None else equilirium_idx
        
        
        control = self.opt_control if control is None else control
        traj = self.opt_traj if traj is None else traj    
        
        S = traj
        
        plt.figure(figsize=(12,4))

        plt.subplot(131)
        plt.plot(self.time_window, S,label='S')
        plt.plot(self.time_window[equilirium_idx], traj[equilirium_idx],'b.')
        plt.plot(self.time_window[[0,-1]], 2*[self.S_star],'r--',label='Equilibrium val. $S^\\star$')
        plt.xlabel('t')
        plt.title('(a) Stock time serie')
        plt.legend();

        plt.subplot(132)
        plt.plot(self.time_window, control,label='x')
        plt.plot(self.time_window[equilirium_idx], control[equilirium_idx],'b.')
        plt.plot(self.time_window[[0,-1]], 2*[self.x_star],'r--',label='Equilibrium val. $x^\\star$')
        plt.ylim(0,1.5)
        plt.title('(b) Extraction time serie')
        plt.xlabel('t')
        plt.legend()

        plt.subplot(133)
        plt.plot(control, S,label='opt. traj')
        plt.plot(control[0], traj[0],'r.',label='initial cond')
        plt.plot(control[equilirium_idx], traj[equilirium_idx],'b.',label='apparent Equili.')
        plt.plot(self.x_star,self.S_star,'g.',label='th Equili.')
        plt.xlabel('x (extraction)')
        plt.ylabel('S (atm. co2)')
        plt.title('(c) Phase plan')
        plt.legend();



class HoelKverndokk(SimplifiedHoelKverndokk):
    '''
    Simplified version of the Hoel and Kverndokk model where the social welfare is given
    as an utility `u(x)` function of the extraction and consumption of an exhaustible 
    ressource (fossil fuel) whose consumption realeases carbon in the atmosphere,
    minus a damage function `D(S)` where `S` denotes the atmospheric stock of carbon.
    Here the damage function is defined as 

    $$ D(S) = ω S^2 $$

    This implementation is similar to Eq.(1), where the utility is a shifted CRRA utility
    u(x)=u_γ(x+ϕ), and the marginal cost of extraction is defined as 

    $$ c(A) = c_1+c_2 A^2 $$
    
    References
    ---
    
    M. Hoel and S. Kverndokk, “Depletion of fossil fuels and the impacts of global warming,” 
    Resource and Energy Economics, vol. 18, no. 2, pp. 115–136, Jun. 1996, 
    doi: 10.1016/0928-7655(96)00005-x.
    
    '''
    
    def __init__(self, *args, c_1=1.2, c_2=1.5, ϕ=0.1, **kwargs):               
        super().__init__(*args, **kwargs)                       
        # Marginal extraction cost parameters
        self._c_1 = c_1
        self._c_2 = c_2
        # Phase shift for utility function
        self.ϕ = ϕ  # Phase shift of utility                  / ϕ = 0.1   / 
                
    def u(self, x):
        """ Shifted CRRA utility function """
        return super().u(x+self.ϕ)
        
    def c(self, A):
        """ Marginal cost of extraction """
        return self._c_1+self._c_2*np.power(A,2)
    
    def trend(self, t, state):
        S, A = state
        xt = self.control(t)
        dS = xt - self.δ*S
        dA = xt
        return np.array([dS,dA])
    
    def societal_utility(self, control, traj):
        traj = np.asarray(traj)
        S = traj[:,0]
        A = traj[:,1]
        x = control        
        return (self.u(x)-self.c(A)*x-self.damage(S) )*np.power(self.β,self.time_window)

    def plot_traj(self, equilirium_idx = None, control=None, traj=None):
        """
        Plot of the economical path in the reduced formulation of the HK model.
        When control and traj are None, the path is the optimal one
        """
        
        equilirium_idx = self.ndt//2 if equilirium_idx is None else equilirium_idx
        
        
        control = self.opt_control if control is None else control
        traj = self.opt_traj if traj is None else traj    
        
        traj = np.asarray(traj)
        
        S = traj[:,0]
        A = traj[:,1]
        
        plt.figure(figsize=(14,4))
        plt.subplot(141)
        plt.plot(self.time_window, S,label='S')
        plt.plot(self.time_window[equilirium_idx], S[equilirium_idx],'b.')
        plt.plot(self.time_window[[0,-1]], 2*[self.S_star],'r--',label='Equilibrium val. $S^\\star$')
        plt.xlabel('t')
        plt.title('(a) Stock time serie')
        plt.legend();

        plt.subplot(142)
        plt.plot(self.time_window, control,label='x')
        plt.plot(self.time_window[equilirium_idx], control[equilirium_idx],'b.')
        plt.plot(self.time_window[[0,-1]], 2*[self.x_star],'r--',label='Equilibrium val. $x^\\star$')
        plt.ylim(0,1.5)
        plt.title('(b) Extraction time serie')
        plt.xlabel('t')
        plt.legend()
        
        plt.subplot(143)
        plt.plot(self.time_window, A,label='A')    
        plt.title('(c) Cumulative extraction')
        plt.xlabel('t')
        plt.legend()
        

        plt.subplot(144)
        plt.plot(control, S,label='opt. traj')
        plt.plot(control[0], S[0],'r.',label='initial cond')
        plt.plot(control[equilirium_idx], S[equilirium_idx],'b.',label='apparent Equili.')
        # No equilibrium in that case
        #plt.plot(self.x_star,self.S_star,'g.',label='th Equili.')
        plt.xlabel('x (extraction)')
        plt.ylabel('S (atm. co2)')
        plt.title('(d) Phase plan')
        plt.legend();

