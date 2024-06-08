"""
Author : Olivier Pannekoucke
Creation Date :  2024-03-26 
Modifications : None
"""
import numpy as np
from .socialplanner import SocialPlanner
import matplotlib.pyplot as plt

class Ramsey(SocialPlanner):
    '''
    Economical model that represent
    '''
    
    def __init__(self, *args, γ=2., ρ=0.015, α=0.33, δ=0.1, n=0.01, β=None,**kwargs):        
        super().__init__(*args, **kwargs)        
        self.γ = γ  # Elasticity of intertemporal substitution  / γ = 2 / 
                    # Rate of inequality aversion
        self.δ = δ  # Depreciation rate of the capital          / δ = 0.1 /  
        self.ρ = ρ  # Discount rate for intertemporal utility   / ρ = 0.015 / 
        self.α = α  # Elasticity GDP/Capital in the Cobb-Douglas GDP / α = 0.33 / 
        self.A = 1. # Total productivity factor, that is the technology/innovation / A=1 / 
        self.n = n  # Population growth rate        
        self.β = np.exp(-(self.ρ-self.n)*self.dt) if β is None else β # is the discount factor  / β = 0.95 
        
    def f(self, k):
        """
        Growth Domestic Production (PIB in french)
        """
        return self.A * np.power(k,self.α) 
                                         
    def u(self,c):
        """
        Utility function
        """
        γ = self.γ
        if γ==1.:
            return np.log(c)
        else:
            return np.power(c,1.-γ)/(1.-γ)
        
    def u_prime(self,c):
        h = 1e-7
        return np.imag(self.u(c+1j*h)/h)         

    def trend(self, t, state):
        k = state
        y = self.f(k)
        investment = y*(1-self.control(t))
        return investment-(self.δ+self.n)*k

    
    def societal_utility(self, control, traj):
        '''
        c : compstion rate (1-c) being the saving rate.
        k : capital per person.
        '''
        c = control
        k = traj
        consumption = c*self.f(k)        
        return np.sum(self.u(consumption)*np.power(self.β,self.time_window) )
        
    @property
    def k_max(self):
        ''' Maximum value for which the consumption is non-negative '''
        return (self.A/(self.n+self.δ))**(1/(1-self.α))

    @property
    def k_star(self):
        ''' Equilibrium value for the captial per head '''
        return (self.α*self.A/(self.ρ+self.δ))**(1/(1-self.α))
    
    @property    
    def c_star(self):
        ''' Equilibrium value for the consumption per head '''
        return self.f(self.k_star)-(self.n+self.δ)*self.k_star        
        
    def plot_traj(self, k0=None, c=None):
        '''
        k0 : initial capital value
        c  : plan of consumption rate that ranges within [0,1]
        Optimal traj is plot when optimization has been conducted and c=None
        '''        
        if c is None:
            c = self.opt_control
        if k0 is None:
            k0 = self.opt_traj[0]
            
        k = self.predict(k0, c)
        fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,5))
        ax1.plot(self.time_window, k)
        ax1.plot(self.time_window[[0,-1]], 2*[self.k_star],'r--',label='Equilibrium val. $k^\\star$')
        ax1.set_xlabel('time')
        ax1.set_title('(a) Captial per head')        
        ax1.legend()
        ax2.plot(self.time_window, c)
        ax2.plot(self.time_window[[0,-1]], 2*[self.c_star/self.f(self.k_star)],'r--',label='Equilibrium val. $c^\\star$ ratio')
        ax2.legend()
        ax2.set_xlabel('time')
        ax2.set_title('(b) Consumption rate (in $[0,1]$)')
        
            
    def plot_phase_plan(self):
        k = np.linspace(0,self.k_max,200)        
        # locus \dot k = 0:
        plt.plot(k, self.f(k)-(self.n+self.δ)*k,label='locus $\\dot k = 0$')
        # locus \doc c = 0
        plt.plot(2*[self.k_star],[0,2],label='locus $\\dot c = 0$')
        # Equilibrium
        plt.plot(self.k_star, self.c_star,'b.',label='Equilibium $(k^\\ast,c^\\ast)$')
        plt.xlabel('Capital per head (k or $K/L$)')
        plt.ylabel('Consumption per head (c or $C/L$)')
        plt.legend()    

    def plot_opt_traj(self):    
        '''
        Plot the optimal trajectory in the phase plan
        '''
        self.plot_phase_plan()
        c = self.opt_control
        k = self.predict(k0, c)
        plt.plot(k[0], c[0]*self.f(k[0]),'r.', label='Opt. init. cond.')        
        plt.plot(k, c*self.f(k),'--', color='orange', label='Opt. path')
        plt.legend()
        plt.title('Optimal (k,c) path in the phase plan')
