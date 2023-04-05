import numpy as np
import time
from ene300.functions import function_counter

# Particle Swarm Optimization (PSO)
class PSO:
    def __init__(self):
        pass

    def __call__(self, objective_function, position_boundary, velocity_boundary, weight_function, C_function, population, itmax, max_fa, direction='minimize'):
        ini_time = time.process_time()

        objective_function_ = objective_function
        @function_counter
        def objective_function(x):
            if direction == 'minimize':
                return objective_function_(x)
            elif direction == 'maximize':
                return - objective_function_(x)

        self.R1s = []  
        self.R2s = []  
        self.C1s = []  
        self.C2s = []

        self.weight_function = weight_function
        self.weights = []
        for key, value in list(weight_function.items())[1:]: 
            self.__setattr__(key, value )

        #C = acceleration_coefficient

        position_boundary = np.array(position_boundary)
        velocity_boundary = np.array(velocity_boundary)


        dimensions = len(position_boundary)

        position = np.zeros((dimensions, population))
        velocity = np.zeros((dimensions, population))
        fit = np.zeros(population)

        min_position = position_boundary[:,0]
        max_position = position_boundary[:,1]

        min_velocity = velocity_boundary[0]
        max_velocity = velocity_boundary[1]

        for i in range(population):
            position[:,i] = min_position + np.random.rand(dimensions)*(max_position-min_position)
            velocity[:,i] = min_velocity + np.random.rand(dimensions)*(max_velocity-min_velocity)
            
        fit = objective_function(position)

        position_best = position
        best_fit = np.min(fit)
        best_fit_idx = np.argmin(fit)
        global_best = position[:, best_fit_idx]


        
        history = {}
        history['iteration'] = []
        history['position'] = []
        history['velocity'] = []
        history['position_best'] = []
        history['global_best'] = []
        history['best_fit'] = []
        history['cpu_time'] = []
        history['position_boundary'] = position_boundary
        history['objective_function'] = objective_function_
        history['population'] = population
        history['itmax'] = itmax
        history['function_evaluations'] = 0
        history['max_fa'] = max_fa
        history['directon'] = direction


        self.itmax = itmax
        it = 0
        break_flag = False
        while it < itmax and break_flag is False:
            it += 1
            self.it = it
            #weight = max_weight - (max_weight-min_weight) * it/itmax
            #weight = self._weight_function()
            weight = self._get_function(weight_function)
            self.weights.append(weight)


            for i in range(population):
                R1 = np.random.rand()
                #R1 = self._get_function(R_function[0])
                R2 = np.random.rand()
                #R2 = self._get_function(R_function[1])
                
                C1 = self._get_function(C_function[0])
                C2 = self._get_function(C_function[1])
                
                velocity[:, i] = weight*velocity[:,i]+C1*R1*(position_best[:, i]- position[:,i])+C2*R2*(global_best[:]- position[:,i])

                for j in range(dimensions):
                    velocity[j,:] = np.clip(velocity[j,:], *velocity_boundary)

                position[:,i] = position[:,i] + velocity[:,i]

                for j in range(dimensions):
                    position[j,:] = np.clip(position[j,:], *position_boundary[j])

            new_fit = objective_function(position)

            for i in range(population):
                if new_fit[i] < fit[i]:
                    fit[i] =  np.copy(new_fit[i])
                    position_best[:,i] = np.copy(position[:,i])
                
                if fit[i] < best_fit:
                    best_fit = np.copy(fit[i])
                    global_best = np.copy(position_best[:,i])
                
            self.R1s.append(R1)
            self.R2s.append(R2)
            self.C1s.append(C1)
            self.C2s.append(C2)

            if direction == 'maximize':
                best_fit = -best_fit
                
            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['velocity'].append(np.copy(velocity))
            history['position_best'].append(np.copy(position_best))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))

            if objective_function.calls >= max_fa:
                break_flag = True
                break

        self.weight = np.array(self.weights)
        self.R1= np.array(self.R1s)
        self.R2 = np.array(self.R2s)
        self.C1 = np.array(self.C1s)
        self.C2 = np.array(self.C2s)
            
        cpu_time = time.process_time() - ini_time
        history['cpu_time'] = cpu_time
        history['function_evaluations'] = objective_function.calls
        
        return global_best, best_fit, history
        
    def error_metric(self, x_ii, x_i):
        return abs(x_ii-x_i)

    def _weight_function(self):
        if self.weight['function'] == 'constant':
            weight = self.weight['constant']

        elif self.weight['function']== 'random':
            weight = 0.5 + np.random.rand()/2

        elif self.weight['function'] == 'linear_decrease':
            t = self.it-1
            tmax = self.itmax
            weight = self.weight['max'] - (self.weight['max'] -self.weight['min']) * t / tmax

        elif self.weight['function'] == 'sigmoidal_increase':
            gen = self.itmax
            t = self.it-1
            tmax = self.itmax
            n = self.n
            u_sign = self.u_sign
        
            u = 10**(np.log(gen)-2)
            weight = (self.weight['start'] - self.weight['end'])/(1+np.exp(u_sign*(t-n*tmax)))
        

        return weight

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