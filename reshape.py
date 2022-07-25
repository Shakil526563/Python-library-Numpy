# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:32:10 2022

@author: WIN10
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
ar=arr.reshape(4,3)

newarr = arr.reshape(3, 2,2)
"""2,2 array maek 3 time """
print(ar)
print(newarr)