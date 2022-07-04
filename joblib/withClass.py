import time
import numpy as np
from math import sqrt
from joblib import Parallel, delayed

def myFunction( theClass):
    theClass.doASum()
    return theClass.finalSum


class AClass:
    def __init__(self,x):
        self.x = x

    def doASum(self ):
        sum = 0
        for i in range(self.x[0],self.x[1]+1 ):
            sum += (1.0*i)**(1./self.exponent)
        self.finalSum = sum

task = 10000000
size = 12

args = [ [task*(i-1)+1,task*i] for i in range(1,size+1)]
myClasses = []
for i in range(0,size):
    myClass = AClass( args[i])
    myClass.exponent = 40.0
    myClasses.append( myClass )
    

t = time.time()
results= Parallel(n_jobs=2)(delayed(myFunction)(myClasses[i] ) for i in range(size))
print(time.time() - t)
print( sum( results ))

