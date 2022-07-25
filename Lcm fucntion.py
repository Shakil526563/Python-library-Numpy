# -*- coding: utf-8 -*-
"""
The Lowest Common Multiple is the least number that is common multiple of both of the numbers.

"""

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
y=np.arange(1,10)
z=np.lcm.reduce(y)

print(x)
print(z)