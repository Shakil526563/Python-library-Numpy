# -*- coding: utf-8 -*-
"""
The copy SHOULD NOT be affected by the changes made to the original array.
The view SHOULD be affected by the changes made to the original array.
"""

import numpy as np
ar=np.array([1,2,5,8,9,3])
arr=np.array([1,5,8,9])
x=ar.copy()
y=arr.view()
arr[2]=6
ar[1]=5
print(x)
print(ar)
print(y)
print(arr)