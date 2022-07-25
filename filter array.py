# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:55:03 2022

@author: WIN10
"""

import numpy as np

arr = np.array([1, 22, 3, 4, 11, 6, 0, 8])
filter=arr%2==0
print(arr[filter])