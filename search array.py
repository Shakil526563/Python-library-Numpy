# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:48:58 2022

@author: WIN10
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
search=np.where(arr%2==0)
search1=np.searchsorted(arr, 7)
"""array return index just"""
print(search)
"""if you print these value then you assign the index thats array"""
print(arr[search])
print(search1)