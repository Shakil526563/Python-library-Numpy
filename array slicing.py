# -*- coding: utf-8 -*-
"""
array slicing
We pass slice instead of index like this: [start:end].
3: means start a array at 3.4: means end a array before number of 4 index;

We can also define the step, like this: [start:end:step].
"""

import numpy as np
ar=np.array([1,2,5,8,69])
print(ar[1:3])

"""if we use negative index .those negative index count at last position"""
print(ar[-0:-2])
"""if you use step position .step position work jump index,Here index jump 2 step """
print(ar[1:4:2])