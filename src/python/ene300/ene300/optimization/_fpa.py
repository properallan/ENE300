import numpy as np
from scipy.special import gamma
import time

def Levy(d):
    beta = 1.5
    sigma_u = (gamma(1+beta)*np.sin(np.pi*beta/2)/gamma((1+beta)/2)/beta/(2**((beta-1)/2)))**(1/beta)
    sigma_v = 1
    u = np.random.normal(0, sigma_u**2, d)
    v = np.random.normal(0, sigma_v**2, d)
    s = u/(abs(v)**(1/beta))
    L = 1*s
    return L    

# Flower Pollination Algorithm (FPA)
class FPA:
    def __init__(self):
        pass

    def __call__(self, objective_function, position_boundary, population, p, itmax):
        """
        p: change probalility to change from global to local pollination
        """
        
        init_time = time.process_time()

        position_boundary = np.array(position_boundary)
        dimensions = len(position_boundary)

        position = np.zeros((dimensions, population))
        fit = np.zeros(population)

        min_position = position_boundary[:,0]
        max_position = position_boundary[:,1]

        for i in range(population):
            position[:,i] = min_position + np.random.rand(dimensions)*(max_position-min_position)
            fit[i] = objective_function(position[:,i])

        fmin = np.min(fit)
        imin = np.argmin(fit)

        global_best = position[:,imin]
        S = position

        history = {}

        history['iteration'] = []
        history['position'] = []
        history['global_best'] = []
        history['best_fit'] = []
        history['cpu_time'] = []
        history['position_boundary'] = position_boundary
        history['objective_function'] = objective_function
        history['population'] = population
        history['itmax'] = itmax


        for it in range(1,itmax+1):
            for i in range(population):
                if np.random.rand() > p:
                    # global pollination
                    L = Levy(dimensions)
                    dS = L*(position[:,i]-global_best)
                    S[:,i] = position[:,i] + dS
                    # check bounds
                    for j in range(dimensions):
                        S[j,:] = np.clip(S[j,:], *position_boundary[j])

                else:
                    #local pollitanion
                    jj = np.random.permutation(population)
                    eps = np.random.rand()
                    S[:,i] = position[:,i] + eps*(position[:,jj[0]]-position[:,jj[1]])
                    # check bounds again
                    for j in range(dimensions):
                        S[j,:] = np.clip(S[j,:], *position_boundary[j])


                fit_new = objective_function(S[:,i])
                if fit_new < fit[i]:
                    position[:,i] = np.copy(S[:,i])
                    fit[i] = np.copy(fit_new)

                if fit_new < fmin:
                    global_best = np.copy(S[:,i])
                    fmin = np.copy(fit_new)
            
            best_fit = fmin
            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))
        
        return global_best, best_fit, history