'''
Author : Mochammad Ihza Rizky Karim
'''

import numpy as np 

a = np.array([(-1,-2,-1,1),(1,2,3,-1),(1,2,2,-1)])

b = np.zeros((max(a.shape),max(a.shape)))
b[:a.shape[0],:a.shape[1]] = a
a = b
b = np.linalg.det(a)

print(b)
