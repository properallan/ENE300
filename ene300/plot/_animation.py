import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_pso(history):
    fig, ax = plt.subplots()

    velocities = ax.quiver(*history['position'][0], *history['velocity'][0])
    positions = ax.scatter(*history['position'][0])
    global_best = ax.scatter(*history['global_best'][0], alpha=0, label=f"$x^*=(${history['global_best'][0][0]:<8.4f},{history['global_best'][0][1]:<8.4f})") 
    best_fit = ax.scatter(*history['global_best'][0], label=f"$f(x^*)=${history['best_fit'][0]:<8.4f}", color='r')
    ax.set_xlabel(rf'$x_1$')
    ax.set_ylabel(rf'$x_2$')
    L=plt.legend(loc=1)

    def update(it):
        positions.set_offsets(history['position'][it].T)
        velocities.set_offsets(history['position'][it].T)
        velocities.set_UVC(*history['velocity'][it])
        best_fit.set_offsets(history['global_best'][it].T)
        L.get_texts()[0].set_text(f"$x^*=(${history['global_best'][it][0]:<8.4f},{history['global_best'][it][1]:<8.4f})")
        L.get_texts()[1].set_text(f"$f(x^*)=${history['best_fit'][it]:<8.4f}")
        return (positions, velocities,)

    anim = FuncAnimation(fig, update, frames=len(history['iteration']), blit=True, interval=100, repeat=True)

    plt.close()

    from IPython.display import HTML
    return HTML(anim.to_jshtml())

def animate(history):
    fig, ax = plt.subplots()

    
    if 'velocity' in history.keys(): velocities = ax.quiver(*history['position'][0], *history['velocity'][0])
    positions = ax.scatter(*history['position'][0])
    global_best = ax.scatter(*history['global_best'][0], alpha=0, label=f"$x^*=(${history['global_best'][0][0]:<8.4f},{history['global_best'][0][1]:<8.4f})") 
    best_fit = ax.scatter(*history['global_best'][0], label=f"$f(x^*)=${history['best_fit'][0]:<8.4f}", color='r')
    ax.set_xlabel(rf'$x_1$')
    ax.set_ylabel(rf'$x_2$')
    ax.set_ylim(history['position_boundary'][1])
    ax.set_xlim(history['position_boundary'][0])
    L=plt.legend(loc=1)

    def update(it):
        positions.set_offsets(history['position'][it].T)
        if 'velocity' in history.keys():
            velocities.set_offsets(history['position'][it].T)
            velocities.set_UVC(*history['velocity'][it])
        best_fit.set_offsets(history['global_best'][it].T)
        L.get_texts()[0].set_text(f"$x^*=(${history['global_best'][it][0]:<8.4f},{history['global_best'][it][1]:<8.4f})")
        L.get_texts()[1].set_text(f"$f(x^*)=${history['best_fit'][it]:<8.4f}")
        
        if 'velocity' in history.keys():
            return (positions, velocities,)
        else:
            return (positions,)

    anim = FuncAnimation(fig, update, frames=len(history['iteration']), blit=True, interval=100, repeat=True)

    plt.close()

    from IPython.display import HTML
    return HTML(anim.to_jshtml())