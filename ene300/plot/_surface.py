def plot_surface(history, discretization=[200,200], domain=None, **plot_kwargs):
    import numpy as np
    import matplotlib.pyplot as plt

    if domain is None:
        domain = history['position_boundary']

    X1 = np.linspace(domain[0][0], domain[0][1], discretization[0])
    X2 = np.linspace(domain[1][0], domain[1][1], discretization[1])
    X, Y = np.meshgrid(X1, X2)
    Z = history['objective_function']([X, Y])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, **plot_kwargs)

    ax.scatter(*history['global_best'][-1], history['best_fit'][-1], alpha=0, label=f"$x^*=(${history['global_best'][-1][0]:<8.4f},{history['global_best'][-1][1]:<8.4f})") 
    ax.scatter(*history['global_best'][-1], history['best_fit'][-1], label=f"$f(x^*)=${history['best_fit'][-1]:<8.4f}", color='r')
    
    ax.set_xlabel(fr'$x_1$')
    ax.set_ylabel(fr'$x_2$')
    ax.set_zlabel(fr'$f$')

    plt.tight_layout()
    plt.legend()
    plt.show()

def plot_objective_function(objective_function, position_boundary, discretization, optimum=None, save_file=None, regularized_ts=False, **plot_kwargs):
    import numpy as np
    import matplotlib.pyplot as plt

    domain = position_boundary

    X1 = np.linspace(domain[0][0], domain[0][1], discretization[0])
    X2 = np.linspace(domain[1][0], domain[1][1], discretization[1])
    X, Y = np.meshgrid(X1, X2)

    if regularized_ts:
        Z_fix = np.ones_like(X)*249.30934834
        Z = objective_function([X, Y, Z_fix ])
    else:
        Z = objective_function([X, Y])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, **plot_kwargs)

    if optimum:
        if regularized_ts:
            ax.scatter(*tuple(optimum.values()),  alpha=0, label=fr"$\mathbf{{x}}^*=(${optimum['x']:<8.4f},{optimum['y']:<8.4f},{249.30934834:<8.4f})") 
        else:
            ax.scatter(*tuple(optimum.values()),  alpha=0, label=fr"$\mathbf{{x}}^*=(${optimum['x']:<8.4f},{optimum['y']:<8.4f})") 
        ax.scatter(*tuple(optimum.values()),  label=fr"$f(\mathbf{{x}}^*)=${optimum['z']:<8.4f}", color='red')
        #ax.scatter(0, 0, -1, c='r')

    #cbar = fig.colorbar(surf, shrink=0.8)
    #cbar.set_label(fr'$f(\mathbf{{x}})$')#, rotation=270)
    ax.set_xlabel(fr'$x_1$')
    ax.set_ylabel(fr'$x_2$')
    ax.set_zlabel(fr'$f(\mathbf{{x}})$')
    plt.tight_layout()
    plt.legend(frameon=False)    
    plt.tight_layout()
    if save_file:
        plt.savefig(save_file)
    plt.show()