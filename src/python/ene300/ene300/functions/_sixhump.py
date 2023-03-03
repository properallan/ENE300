import numpy as np
from ._function_counter import function_counter

@function_counter
def sixhump(x):
    # Referencia
    #Molga, M., & Smutnicki, C. Test functions for optimization needs (2005). Retrieved June
    #2013, from http://www.zsd.ict.pwr.wroc.pl/files/docs/functions.pdf
    return (4-2.1*x[0]**2+x[0]**4/3)*x[0]**2 + x[0]*x[1]+(-4+4*x[1]**2)*x[1]**2
