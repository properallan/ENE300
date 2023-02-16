
from autograd import grad
import numpy as np

def dichotomous_search(f, a, b, epsilon):
    print(f"it \ta \tb \tintervalo  \tx1 \tx2 \tf_x1   \tf_x2")
    it = 0
    while abs(a - b) >= epsilon*10.0:
        x1 = (a + b)/2.0 - epsilon
        x2 = (a + b)/2.0 + epsilon
        f_x1 = f(x1)
        f_x2 = f(x2)
        if f_x1 > f_x2:
            a = x1
        else:
            b = x2

        it += 1
        erro = abs(a-b)
        
        print(f"{it} \t{a:.4f} \t{b:.4f} \t{erro:.4f}  \t{x1:.4f} \t{x2:.4f} \t{f_x1:.4f} \t{f_x2:.4f}")
    return (a + b) / 2.0

def newton_method(f, x0, epsilon, max_iterations=100):
    df = grad(f)
    d2f = grad(df)
    x = x0
    iteration = 0
    while True:
        f_x = f(x)
        df_x = df(float(x))
        d2f_x = d2f(float(x))
        x_new = x - df_x / d2f_x
        print(f"Iteration {iteration}: x = {x_new}, f(x) = {f_x}")
        if np.abs(x_new - x) < epsilon or iteration >= max_iterations:
            break
        x = x_new
        iteration += 1
    return x_new
