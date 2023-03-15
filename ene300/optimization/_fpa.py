import numpy as np
from scipy.special import gamma
import time
from ene300.functions import function_counter

def Levy(d):
    beta = 1.5
    sigma_u = (gamma(1+beta)*np.sin(np.pi*beta/2)/gamma((1+beta)/2)/beta/(2**((beta-1)/2)))**(1/beta)
    sigma_v = 1
    #tmpdiv = (gamma((1+beta)/2)*beta*2**((beta-1)/2))**(1/beta)
    #sigma = (gamma(1+beta)*np.sin(np.pi*beta/2))/tmpdiv
    u = np.random.normal(0, sigma_u**2, d)
    #u = np.random.rand(d)*sigma
    v = np.random.normal(0, sigma_v**2, d)
    #v = np.random.rand(d)
    step = u/(abs(v)**(1/beta))
    L = 1*step
    return L    

# Flower Pollination Algorithm (FPA)
class FPA:
    def __init__(self):
        pass

    def __call__(self, objective_function, position_boundary, population, p, itmax, max_fa, direction='minimize'):
        """
        p: change probalility to change from global to local pollination
        """
        ini_time = time.process_time()

        objective_function_ = objective_function
        @function_counter
        def objective_function(x):
            if direction == 'minimize':
                return objective_function_(x)
            elif direction == 'maximize':
                return - objective_function_(x)

        position_boundary = np.array(position_boundary)
        dimensions = len(position_boundary)

        position = np.zeros((dimensions, population))
        fit = np.zeros(population)

        min_position = position_boundary[:,0]
        max_position = position_boundary[:,1]

        for i in range(population):
            position[:,i] = min_position + np.random.rand(dimensions)*(max_position-min_position)
        fit = objective_function(position)

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
        history['objective_function'] = objective_function_
        history['population'] = population
        history['itmax'] = itmax
        history['max_fa'] = max_fa
        history['directon'] = direction

        it = 0
        break_flag = False
        while it < itmax and break_flag is False:
            it += 1
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


            fit_new = objective_function(S)
            for i in range(population):
                if fit_new[i] < fit[i]:
                    position[:,i] = np.copy(S[:,i])
                    fit[i] = np.copy(fit_new[i])

                if fit_new[i] < fmin:
                    global_best = np.copy(S[:,i])
                    fmin = np.copy(fit_new[i])
            
                if objective_function.calls >= max_fa:
                    break_flag = True
                    break

            best_fit = fmin
            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))

        cpu_time = time.process_time() - ini_time
        history['cpu_time'] = cpu_time
        history['function_evaluations'] = objective_function.calls
        
        return global_best, best_fit, history