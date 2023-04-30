import numpy as np
import time
from ene300.functions import function_counter
import copy

# Genetic Algorithm
class GA:
    def __init__(self): 
        pass

    def __call__(self, objective_function, position_boundary, population, itmax, max_fa, direction='minimize'):
        self.direction = direction
        ini_time = time.process_time()

        objective_function_ = copy.copy(objective_function)
        @function_counter
        def objective_function(x):
            if direction == 'minimize':
                return -objective_function_(x)
            elif direction == 'maximize':
                return objective_function_(x)
        
        position_boundary = np.array(position_boundary)

        num_chromosomes = population
        num_genes = len(position_boundary)
        
        #sol_per_pop = 8# Defining the population size.
        #num_weights = len(position_boundary)

        chromosome_size = (num_genes, num_chromosomes) # The population will have num_chromosomes chromosome where each chromosome has num_genes genes.

        #Creating the initial population.
        min_genes = position_boundary[:,0]
        max_genes = position_boundary[:,1]

        chromosome = np.zeros(chromosome_size)
        # random initialization of population
        for i in range(num_chromosomes):
            chromosome[:, i] = min_genes + np.random.rand(num_genes)*(max_genes-min_genes)

        num_generations = itmax

        num_parents_mating = 4
        history = {}

        history['iteration'] = []
        history['position'] = []
        history['global_best'] = []
        history['best_fit'] = []
        history['cpu_time'] = []
        history['position_boundary'] = position_boundary
        history['objective_function'] = objective_function_
        history['population'] = num_chromosomes
        history['itmax'] = num_generations
        history['max_fa'] = max_fa
        history['directon'] = direction

        it = 0
        break_flag = False
        while it < itmax and break_flag is False:
            it += 1
            # Measuring the fitness of each chromosome in the population.
            #fitness = ga.cal_pop_fitness(equation_inputs, new_population)
            fitness = objective_function(chromosome)
            # Selecting the best parents in the population for mating.
            
            parents = self.get_best_parents(chromosome, fitness, 
                                            num_parents_mating)
        
            # Generating next generation using crossover.
            offspring_crossover = self.crossover(parents,
                                                offspring_size=(num_genes,chromosome_size[1]-parents.shape[1]))
            
            for j in range(num_genes):
                offspring_crossover[j,:] = np.clip(offspring_crossover[j,:], *position_boundary[j])


            # Adding some variations to the offsrping using mutation.
            offspring_mutation = self.mutation(offspring_crossover)
            
            for j in range(num_genes):
                offspring_mutation[j,:] = np.clip(offspring_mutation[j,:], *position_boundary[j])

            # Creating the new population based on the parents and offspring.
            chromosome[:, 0:parents.shape[1]] = np.copy(parents)
            chromosome[:, parents.shape[1]:] = np.copy(offspring_mutation)

            # store best and iterate
            max_fitness_idx = np.where(fitness == np.max(fitness))
            max_fitness_idx = max_fitness_idx[0][0]
            global_best = np.copy(chromosome[:,max_fitness_idx])
            best_fit = np.copy(fitness[max_fitness_idx])

            if direction == 'minimize':
                best_fit = -best_fit

            history['iteration'].append(it)
            history['position'].append(np.copy(chromosome))
            history['global_best'].append(np.copy(global_best))
            history['best_fit'].append(float(best_fit))
        
            if objective_function.calls >= max_fa:
                break_flag == True
                break
           
        cpu_time = time.process_time() - ini_time
        history['cpu_time'] = cpu_time
        history['function_evaluations'] = objective_function.calls

        return global_best, best_fit, history

    def mutation(self, offspring_crossover):

        # Mutation changes a single gene in each offspring randomly.

        for idx in range(offspring_crossover.shape[1]):

            # The random value to be added to the gene.

            random_value = np.random.uniform(-2.0, 2.0, 1)

            random_idx = np.random.randint(0, offspring_crossover.shape[0])

            offspring_crossover[random_idx, idx] = offspring_crossover[random_idx, idx]*(random_value)

        return offspring_crossover

    def get_best_parents(self, population, fitness_, num_parents):
        # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.

        parents = np.empty(( population.shape[0], num_parents))
        fitness = np.copy(fitness_)
        for parent_num in range(num_parents):

            max_fitness_idx = np.where(fitness == np.max(fitness))

            max_fitness_idx = max_fitness_idx[0][0]

            parents[:,parent_num] = np.copy(population[:,max_fitness_idx])

            
            fitness[max_fitness_idx] = -np.inf
            
        return parents

    def crossover(self, parents, offspring_size):
        offspring = np.empty(offspring_size)
        # The point at which crossover takes place between two parents. Usually, it is at the center.
        crossover_point = np.uint8(offspring_size[1]/2)
    
        for k in range(offspring_size[1]):
            # Index of the first parent to mate.
            parent1_idx = k%parents.shape[1]
            # Index of the second parent to mate.
            parent2_idx = (k+1)%parents.shape[1]
            # The new offspring will have its first half of its genes taken from the first parent.
            offspring[0:crossover_point,k] = np.copy(parents[0:crossover_point, parent1_idx])
            # The new offspring will have its second half of its genes taken from the second parent.
            offspring[crossover_point:,k] = np.copy(parents[crossover_point:,parent2_idx])
        return offspring