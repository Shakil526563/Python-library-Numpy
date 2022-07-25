# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:46:45 2022

@author: WIN10
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
ar=np.vstack((arr1,arr2))
print(ar)
print(arr)