import numpy as np
import time
from ene300.functions import function_counter

# Symbiotic Organisms Search (SOS)
class SOS:
    def __init__(self): 
        pass

    def __call__(self, objective_function, position_boundary, population, itmax):
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


        best_fit = np.min(fit)
        imin = np.argmin(fit)
        global_best = position[:,imin]

        for it in range(1,itmax+1):

            best_fit = np.min(fit)
            imin = np.argmin(fit)
            global_best = np.copy(position[:,imin])
         
            history['iteration'].append(it)
            history['position'].append(np.copy(position))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))
            
            for i in range(population):
                # mutualism
                position, fit = self.mutualism(i, population, position, dimensions, global_best, position_boundary, objective_function, fit)
                # comensalism
                position, fit = self.comensalism(i, population, position, dimensions, global_best, position_boundary, objective_function, fit)
                # parasitism
                position, fit = self.parasitism( i, population, position, dimensions, max_position, min_position, objective_function, fit)
         
        cpu_time = time.process_time() - ini_time
        history['cpu_time'] = cpu_time
        history['function_evaluations'] = objective_function.calls
        

        return global_best, best_fit, history

    def mutualism(self, i, population, position, dimensions, global_best, position_boundary, objective_function, fit):
        j = np.copy(i)
        while i == j:
            seed = np.random.permutation(population)
            j = seed[0]

        #mutual = np.mean([position[:,i], position[:,j]])    
        mutual = (position[:,i] + position[:,j])/2
        bf1 = np.round(1+np.random.rand())
        bf2 = np.round(1+np.random.rand())

        ecoNew1 = position[:,i] + np.random.rand(dimensions)*(global_best-bf1*mutual)
        ecoNew2 = position[:,j] + np.random.rand(dimensions)*(global_best-bf2*mutual)
        
        #for jj in range(dimensions):
        #    ecoNew1[jj,:] = np.clip(ecoNew1[jj,:], *position_boundary[jj])
        #    ecoNew2[jj,:] = np.clip(ecoNew2[jj,:], *position_boundary[jj])

        for jj in range(dimensions):
            ecoNew1[jj] = np.clip(ecoNew1[jj], *position_boundary[jj])
            ecoNew2[jj] = np.clip(ecoNew2[jj], *position_boundary[jj])


        fitNew1 = objective_function(ecoNew1)
        fitNew2 = objective_function(ecoNew2)

        if fitNew1 < fit[i]:
            fit[i] = np.copy(fitNew1)
            position[:, i] = np.copy(ecoNew1)

        if fitNew2 < fit[j]:
            fit[j] = np.copy(fitNew2)
            position[:, j] = np.copy(ecoNew2)
            
        return position, fit
    
    def comensalism(self, i, population, position, dimensions, global_best, position_boundary, objective_function, fit):
        # random chose
        j = np.copy(i)
        while i == j:
            seed=np.random.permutation(population)
            j=seed[0]

        ecoNew1 = position[:,i] + (np.random.rand(dimensions)*2-1)*(global_best-position[:,j])
        #for jj in range(dimensions):
        #    ecoNew1[jj,:] = np.clip(ecoNew1[jj,:], *position_boundary[jj])
        for jj in range(dimensions):
            ecoNew1[jj] = np.clip(ecoNew1[jj], *position_boundary[jj])

        fitNew1 = objective_function(ecoNew1) 

        if fitNew1 < fit[i]:
            fit[i] = np.copy(fitNew1)
            position[:, i] = np.copy(ecoNew1)

        return position, fit

    def parasitism(self, i, population, position, dimensions, max_position, min_position, objective_function, fit):
        j = np.copy(i)
        while i == j:
            seed =np.random.permutation(population)
            j = seed[0]

        parasite = np.copy(position[:, j])
        seed = np.random.permutation(dimensions)
        pick = seed[0:int(np.ceil(np.random.rand()*dimensions))]   
        parasite[pick]= np.random.rand(len(pick))*(max_position[pick]-min_position[pick])+min_position[pick]
        fitParasite = objective_function(parasite)
    
        if fitParasite < fit[j]:
            fit[j] = np.copy(fitParasite)
            position[:,j] = np.copy(parasite)
    

        return position, fit