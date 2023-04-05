import numpy as np
import time
from ene300.functions import function_counter

# Grey Wolf Optimizater (GWO)
class GWO:
    def __init__(self): 
        pass

    def __call__(self, objective_function, position_boundary, population, a_function, itmax, max_fa, direction='minimize'):
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

        # random initialization of population
        for i in range(population):
            position[:,i] = min_position + np.random.rand(dimensions)*(max_position-min_position)
            
        fit = objective_function(position)
        
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

        
        sorted_fit = np.sort(fit)
        sorted_i = np.argsort(fit)

        best_fit = np.copy(sorted_fit[0])

        # calculate fitness of each agent
        alpha = np.copy(position[:, sorted_i[0]])
        beta  = np.copy(position[:, sorted_i[1]])
        delta = np.copy(position[:, sorted_i[2]])

        self.itmax = itmax
        it = 0
        break_flag = False
        while it < itmax and break_flag is False:
            it += 1
            self.it = it
            a = self._get_function(a_function)

            for i in range(3,population):
                #  update position of each search agent
                #  update a, A and C
                position[:,i] = self._update_agent(position[:,i], alpha, beta, delta, a)
            
            # position constraint
            for j in range(dimensions):
                position[j,:] = np.clip(position[j,:], *position_boundary[j])

            # calculate fitness
            fit = objective_function(position)

            sorted_fit = np.sort(fit)
            sorted_i = np.argsort(fit)

            best_fit = np.copy(sorted_fit[0])

            # update alpha, beta and delta
            alpha = np.copy(position[:, sorted_i[0]])
            beta  = np.copy(position[:, sorted_i[1]])
            delta = np.copy(position[:, sorted_i[2]])
         
            # store best and iterate
            global_best = np.copy(alpha)


            if direction == 'maximize':
                best_fit = -best_fit

            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))
        
            if objective_function.calls >= max_fa:
                break_flag == True
                break
           
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

        A1 = (2*a*np.random.rand() - a)
        A2 = (2*a*np.random.rand() - a)
        A3 = (2*a*np.random.rand() - a)

        D_alpha = np.abs(C1*alpha -position)
        D_beta  = np.abs(C2*beta  -position)
        D_delta = np.abs(C3*delta -position)
        
        X1 = alpha - A1*(D_alpha)
        X2 = beta  - A2*(D_beta)
        X3 = delta - A3*(D_delta)

        X = (X1 + X2 + X3)/3.0

        return X