import numpy as np
import time
from ene300.functions import function_counter

# Symbiotic Organisms Search (SOS)
class SOS:
    def __init__(self): 
        pass

    def __call__(self, objective_function, position_boundary, population, itmax, max_fa, direction='minimize'):
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

        # random initialization
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


        best_fit = np.min(fit)
        imin = np.argmin(fit)
        global_best = position[:,imin]

        it = 0
        self.itmax = itmax
        self.break_flag = False
        while it < self.itmax and self.break_flag is False:
            it += 1

            best_fit = np.min(fit)
            imin = np.argmin(fit)
            global_best = np.copy(position[:,imin])
         
            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))
            
            if objective_function.calls+1 >= max_fa:
                self.break_flag = True
                break
            # mutualism
            position, fit = self.mutualism(population, position, dimensions, global_best, position_boundary, objective_function, fit)
            if objective_function.calls >= max_fa:
                self.break_flag = True
                break
            # comensalism
            position, fit = self.comensalism(population, position, dimensions, global_best, position_boundary, objective_function, fit)
            if objective_function.calls >= max_fa:
                self.break_flag = True
                break
            # parasitism
            position, fit = self.parasitism(population, position, dimensions, max_position, min_position, position_boundary, objective_function, fit)
            if objective_function.calls >= max_fa:
                self.break_flag = True
                break
         
        cpu_time = time.process_time() - ini_time
        history['cpu_time'] = cpu_time
        history['function_evaluations'] = objective_function.calls
        

        return global_best, best_fit, history

    def mutualism(self, population, position, dimensions, global_best, position_boundary, objective_function, fit):
        ecoNew1 = np.zeros_like(position)
        ecoNew2 = np.zeros_like(position)

        for i in range(population):
            j = np.copy(i)
            while i == j:
                seed = np.random.permutation(population)
                j = seed[0]

            #mutual = np.mean([position[:,i], position[:,j]])    
            mutual = (position[:,i] + position[:,j])/2
            bf1 = np.round(1+np.random.rand())
            bf2 = np.round(1+np.random.rand())

            ecoNew1[:,i] = position[:,i] + np.random.rand(dimensions)*(global_best-bf1*mutual)
            ecoNew2[:,i] = position[:,j] + np.random.rand(dimensions)*(global_best-bf2*mutual)
            
            for jj in range(dimensions):
                ecoNew1[jj,:] = np.clip(ecoNew1[jj,:], *position_boundary[jj])
                ecoNew2[jj,:] = np.clip(ecoNew2[jj,:], *position_boundary[jj])

            #for jj in range(dimensions):
            #    ecoNew1[jj] = np.clip(ecoNew1[jj], *position_boundary[jj])
            #    ecoNew2[jj] = np.clip(ecoNew2[jj], *position_boundary[jj])

        fitNew1 = objective_function(ecoNew1)
        fitNew2 = objective_function(ecoNew2)

        for i in range(population):
            if fitNew1[i] < fit[i]:
                fit[i] = np.copy(fitNew1[i])
                position[:, i] = np.copy(ecoNew1[:, i])

            if fitNew2[i] < fit[i]:
                fit[i] = np.copy(fitNew2[i])
                position[:, i] = np.copy(ecoNew2[:, i])
        
        return position, fit
        
    def comensalism(self, population, position, dimensions, global_best, position_boundary, objective_function, fit):
        ecoNew1 = np.zeros_like(position)
        # random chose
        for i in range(population):
            j = np.copy(i)
            while i == j:
                seed=np.random.permutation(population)
                j=seed[0]

            ecoNew1[:,i] = position[:,i] + (np.random.rand(dimensions)*2-1)*(global_best-position[:,j])
            #for jj in range(dimensions):
            #    ecoNew1[jj,:] = np.clip(ecoNew1[jj,:], *position_boundary[jj])
            for jj in range(dimensions):
                ecoNew1[jj,:] = np.clip(ecoNew1[jj,:], *position_boundary[jj])

        fitNew1 = objective_function(ecoNew1) 

        for i in range(population):
            if fitNew1[i] < fit[i]:
                fit[i] = np.copy(fitNew1[i])
                position[:, i] = np.copy(ecoNew1[:,i])

        return position, fit

    def parasitism(self, population, position, dimensions, max_position, min_position, position_boundary, objective_function, fit):
        parasite = np.zeros_like(position)

        for i in range(population):
            j = np.copy(i)
            while i == j:
                seed =np.random.permutation(population)
                j = seed[0]

            parasite[:,i] = np.copy(position[:, j])
            seed = np.random.permutation(dimensions)
            pick = seed[0:int(np.ceil(np.random.rand()*dimensions))]   
            parasite[:,pick]= np.random.rand(len(pick))*(max_position[pick]-min_position[pick])+min_position[pick]
        
        for jj in range(dimensions):
                parasite[jj,:] = np.clip(parasite[jj,:], *position_boundary[jj])

        fitParasite = objective_function(parasite)
        
        for i in range(population):
            if fitParasite[i] < fit[i]:
                fit[i] = np.copy(fitParasite[i])
                position[:,i] = np.copy(parasite[:,i])
        
        return position, fit