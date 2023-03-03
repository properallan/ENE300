import numpy as np
from ._function_counter import function_counter

@function_counter
def eggholder(x):
    # Reference
    # Global Optimization Test Problems. Retrieved June 2013, from http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm. 
    # EASOM FUNCTION Funções para testes de Algoritmos
    y = x[1]
    x = x[0]
    return -(y + 47) * np.sin(np.sqrt(np.abs(x/2 + y + 47))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))
