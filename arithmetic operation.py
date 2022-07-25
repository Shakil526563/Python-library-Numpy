# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:06:48 2022

@author: WIN10
"""

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

add = np.add(arr1, arr2)
sub=np.subtract(arr1,arr2)
diff=np.divide(arr1,arr2)
mul=np.multiply(arr1,arr2)
power=np.power(arr1,arr2)
mod=np.mod(arr1,arr2)
absul=np.absolute(arr1,arr2)

print(add)
print(sub)
print(diff)
print(mul)