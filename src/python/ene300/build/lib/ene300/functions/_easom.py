import numpy as np
from ._function_counter import function_counter

@function_counter
def easom(x):
    # Reference
    # Global Optimization Test Problems. Retrieved June 2013, from http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm. 
    # EASOM FUNCTION Funções para testes de Algoritmos
    return -np.cos(x[0])*np.cos(x[1])*np.exp(-(x[0]-np.pi)**2-(x[1]-np.pi)**2)
