import numpy as np
import time
from ene300.functions import function_counter

# Grey Wolf Optimizater (GWO)
class GWO:
    def __init__(self): 
        pass

    def __call__(self, objective_function, position_boundary, population, itmax, a_function):
        ini_time = time.process_time()

        objective_function_ = objective_function
        @function_counter
        def objective_function(x):
            return objective_function_(x)

        position_boundary = np.array(position_boundary)
        dimensions = len(position_boundary)

        position = np.zeros((dimensions, population))
        fit = np.zeros(population)

        min_position = position_boundary[:,0]
        max_position = position_boundary[:,1]

        # random initialization
        for i in range(population):
            position[:,i] = min_position + np.random.rand(dimensions)*(max_position-min_position)
            fit[i] = objective_function(position[:,i])
        
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

        
        sorted_fit = np.sort(fit)
        sorted_i = np.argsort(fit)

        best_fit = np.copy(sorted_fit[0])

        alpha = np.copy(position[:, sorted_i[0]])
        beta  = np.copy(position[:, sorted_i[1]])
        delta = np.copy(position[:, sorted_i[2]])

        self.itmax = itmax
        for it in range(1,itmax+1):
            self.it = it
            a = self._get_function(a_function)

            for i in range(population):
                position[:,i] = self._update_agent(position[:,i], alpha, beta, delta, a)

            fit = objective_function(position)

            sorted_fit = np.sort(fit)
            sorted_i = np.argsort(fit)

            best_fit = np.copy(sorted_fit[0])

            alpha = np.copy(position[:, sorted_i[0]])
            beta  = np.copy(position[:, sorted_i[1]])
            delta = np.copy(position[:, sorted_i[2]])
         
            global_best = np.copy(alpha)

            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))
           
        cpu_time = time.process_time() - ini_time
        history['cpu_time'] = cpu_time
        history['function_evaluations'] = objective_function.calls
        

        return global_best, best_fit, history

    def _get_function(self, function_dict):
        if function_dict['function'] == 'constant':
            weight = function_dict['constant']

        elif function_dict['function']== 'random':
            weight = 0.5 + np.random.rand()/2

        elif function_dict['function'] == 'linear_decrease':
            t = self.it-1
            tmax = self.itmax
            weight = function_dict['max'] - (function_dict['max'] -function_dict['min']) * t / tmax

        elif function_dict['function'] == 'sigmoidal_increase':
            gen = self.itmax
            t = self.it-1
            tmax = self.itmax
            
            n = function_dict['n']
            u_sign = function_dict['u_sign']
        
            u = 10**(np.log(gen)-2)
            weight = (function_dict['start'] - function_dict['end'])/(1+np.exp(u_sign*(t-n*tmax))) + function_dict['end']
        else:
            raise NotImplementedError(f"Function {function_dict['function']} not implemented in pso.get_function(self, function_dict)")

        return weight

    def _update_agent(self, position, alpha, beta, delta, a):
        C1 = 2*np.random.rand()
        C2 = 2*np.random.rand()
        C3 = 2*np.random.rand()

        D_alpha = np.abs(C1*alpha-position)
        D_beta  = np.abs(C2*beta- position)
        D_delta = np.abs(C3*delta-position)

        A1 = (2*a*np.random.rand() - a)
        A2 = (2*a*np.random.rand() - a)
        A3 = (2*a*np.random.rand() - a)
        
        X1 = alpha - A1*(D_alpha)
        X2 = beta  - A2*(D_beta)
        X3 = delta - A3*(D_delta)

        X = (X1 + X2 + X3)/3.0

        return X