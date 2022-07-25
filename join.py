# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:44:22 2022

@author: WIN10
"""

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
ar=np.concatenate((arr1,arr2),axis=0)
print(ar)