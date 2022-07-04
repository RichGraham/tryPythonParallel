import time
import numpy as np
from math import sqrt
from joblib import Parallel, delayed

task = 300000

def myFunction( x ):
    sum = 0
    for i in range(task * x):
        sum += np.exp( pow(i,1/task))
    return sum


size = 12

t = time.time()
results= Parallel(n_jobs=3)(delayed(myFunction)(i ) for i in range(size))
print(time.time() - t)
print(results)

t = time.time()
results= Parallel(n_jobs=4)(delayed(myFunction)(i ) for i in range(size))
print(time.time() - t)
print(results)

