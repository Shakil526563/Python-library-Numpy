# -*- coding: utf-8 -*-
"""
here ndmin create array dimension,, """

import numpy as np


ar = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(ar.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)