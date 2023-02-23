import numpy as np

# Particle Swarm Optimization (PSO)
def pso(objective_function, position_boundary, velocity_boundary, weight_boundary, acceleration_coefficient, population, itmax):
    C = acceleration_coefficient

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


    min_weight = weight_boundary[0]
    max_weight = weight_boundary[-1]

    C1 = C[0]
    C2 = C[1]

    
    history = {}
    history['iteration'] = []
    history['position'] = []
    history['velocity'] = []
    history['position_best'] = []
    history['global_best'] = []
    history['best_fit'] = []

    for it in range(1,itmax+1):

        weight = max_weight - (max_weight-min_weight) * it/itmax
        for i in range(population):
            R1 = np.random.rand()
            R2 = np.random.rand()
            
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
               

        history['iteration'].append(it)
        history['position'].append(np.copy(position))
        history['velocity'].append(np.copy(velocity))
        history['position_best'].append(np.copy(position_best))
        history['global_best'].append(np.copy(global_best))
        history['best_fit'].append(np.copy(best_fit))
        
    return global_best, best_fit, history

    