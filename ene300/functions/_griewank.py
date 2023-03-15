import numpy as np
from ._function_counter import function_counter

@function_counter
def griewank(x):
    # References
    """
    Global Optimization Test Problems. Retrieved June 2013, from http://www-
    optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm.
    Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June
    2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf
    Funções para testes de Algoritmos
    """
    d = len(x)
    f = 0
    sum = 0
    prod = 1
    for i in range(0, d):
        sum += x[i]**2/4000.0
        prod *= np.cos(x[i]/np.sqrt(i+1)) 
    f = sum - prod + 1
    return f