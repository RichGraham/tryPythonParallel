import time
import numpy as np
from math import sqrt
from joblib import Parallel, delayed

task = 500000

def myFunction( x ):
    sum = 0
    for i in range(task ):
        sum += np.exp( pow(x,1.5*i/task))
    return sum


size = 12

t = time.time()
results= Parallel(n_jobs=1)(delayed(myFunction)(1.1 ) for i in range(size))
print(time.time() - t)
print(results)

t = time.time()
results= Parallel(n_jobs=2)(delayed(myFunction)( 1.1 ) for i in range(size))
print(time.time() - t)
print(results)

