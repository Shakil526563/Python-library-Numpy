# -*- coding: utf-8 -*-
"""
The floor() function rounds off decimal to nearest lower integer.
The ceil() function rounds off decimal to nearest upper integer.

E.g. ceil of 3.166 is 4.
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

E.g. round off to 1 decimal point, 3.16666 is 3.2
"""

import numpy as np

arr = np.floor([-3.1666, 3.6667])

arr1 = np.ceil([-3.1666, 3.6667])
arr2= np.around(3.1666, 2)
print(arr)
print(arr1)
print(arr2)