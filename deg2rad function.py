# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:29:44 2022

@author: WIN10
"""

import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)
y=np.cos(arr)

print(x)
print(y)