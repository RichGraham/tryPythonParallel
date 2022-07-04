import time
from math import sqrt
from joblib import Parallel, delayed

t = time.time()
results= Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(10))


size = 300000

t = time.time()
results= Parallel(n_jobs=1)(delayed(sqrt)(i ** 2) for i in range(size))
print(time.time() - t)
#print(results)



t = time.time()
results= Parallel(n_jobs=4)(delayed(sqrt)(i ** 2) for i in range(size))
print(time.time() - t)
#print(results)

