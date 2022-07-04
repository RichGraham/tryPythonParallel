import time
import numpy as np
from math import sqrt
from joblib import Parallel, delayed

task = 5000000

def myFunction( x ):
    sum = 0
    for i in range(x[0],x[1]+1 ):
        sum += (1.0*i)**(1./40.0)
    return sum


size = 12



args = [ [task*(i-1)+1,task*i] for i in range(1,size+1)]
print(args)

t = time.time()
results= Parallel(n_jobs=4)(delayed(myFunction)(args[i] ) for i in range(size))
print(time.time() - t)
#print(results)
print( sum( results ))

