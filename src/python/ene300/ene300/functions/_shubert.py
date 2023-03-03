import numpy as np
from ._function_counter import function_counter

@function_counter
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