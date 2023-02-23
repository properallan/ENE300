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