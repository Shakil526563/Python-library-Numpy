# -*- coding: utf-8 -*-
"""
The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""

import numpy as np
def fuc(x,y):
   return x*y

f=np.frompyfunc(fuc,2,1)
print(f([2,5,3,6],[5,8,4,7]))