# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:25:09 2022

@author: WIN10
"""

# -*- coding: utf-8 -*-
"""
The Lowest Common Multiple is the least number that is common multiple of both of the numbers.

"""

import numpy as np

num1 = 4
num2 = 6

x = np.gcd(num1, num2)
y=np.arange(1,10)
z=np.gcd.reduce(y)

print(x)
print(z)