import multiprocess as mp  
import time  
import pyDOE
import numpy as np

class someParams:
    def __init__(self, x,y,initialSeed):
        self.x = x
        self.y = y
        self.initialSeed = initialSeed

    def getLHC(self,seedIncrement):
        x=self.x
        y=self.y
        np.random.seed( self.initialSeed + seedIncrement )
        myLHC =  pyDOE.lhs(x,samples=y)
        return sum([sum(i) for i in myLHC])/x/y-0.5


myClass = someParams( 5,5,2)
myPool = mp.Pool(4)  
results = myPool.map(myClass.getLHC, [i for i in range(4)])  
myPool.close()  
myPool.join()
print(results)



myClass = someParams( 5,5,2)
myPool = mp.Pool(4)  
results = myPool.map(myClass.getLHC, [i for i in range(4)])  
myPool.close()  
myPool.join()
print(results)


myClass = someParams( 5,5,3)
myPool = mp.Pool(4)  
results = myPool.map(myClass.getLHC, [i for i in range(4)])  
myPool.close()  
myPool.join()
print(results)

myClass = someParams( 5,5,3)
myPool = mp.Pool(4)  
results = myPool.map(myClass.getLHC, [i for i in range(4)])  
myPool.close()  
myPool.join()
print(results)

myClass = someParams( 5,5,2)
myPool = mp.Pool(4)  
results = myPool.map(myClass.getLHC, [i for i in range(4)])  
myPool.close()  
myPool.join()
print(results)


myClass = someParams( 5000,5000,3)
myPool = mp.Pool(4)  
results = myPool.map(myClass.getLHC, [i for i in range(4)])  
myPool.close()  
myPool.join()
print(results)


