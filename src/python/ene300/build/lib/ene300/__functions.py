import numpy as np

def shubert(x):
    # Reference
    # http://wwwoptima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm
    f = 1
    for d in range(2):
        sum = 0
        for i in range(1, 6):
            sum +=  i * np.cos((i + 1) * x[d] + i)
        f *= sum
    return f

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

def sixhump(x):
    # Referencia
    #Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June
    #2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf
    return (4-2.1*x[0]**2+x[0]**4/3)*x[0]**2 + x[0]*x[1]+(-4+4*x[1]**2)*x[1]**2

def easom(x):
    # Reference
    # Global Optimization Test Problems. Retrieved June 2013, from http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm. 
    # EASOM FUNCTION Funções para testes de Algoritmos
    return -np.cos(x[0])*np.cos(x[1])*np.exp(-(x[0]-np.pi)**2-(x[1]-np.pi)**2)

def eggholder(x):
    # Reference
    # Global Optimization Test Problems. Retrieved June 2013, from http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm. 
    # EASOM FUNCTION Funções para testes de Algoritmos
    y = x[1]
    x = x[0]
    return -(y + 47) * np.sin(np.sqrt(np.abs(x/2 + y + 47))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))
