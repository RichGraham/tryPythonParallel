import pyDOE
import numpy as np
import importlib

multiprocess_spec = importlib.util.find_spec("multiprocess")
foundMultiprocess =  multiprocess_spec is not None

if( foundMultiprocess ):
    import multiprocess as mp    
else:
    import multiprocessor as mp    


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

number_of_Processors = mp.cpu_count()

print('Found '+str(number_of_Processors)+' processors')
    
myClass = someParams( 5,5,2)
myPool = mp.Pool( number_of_Processors )  
results = myPool.map(myClass.getLHC, [i for i in range(number_of_Processors)])  
myPool.close()  
myPool.join()
print(results)



myClass = someParams( 5,5,2)
myPool = mp.Pool( number_of_Processors)  
results = myPool.map(myClass.getLHC, [i for i in range(number_of_Processors)])  
myPool.close()  
myPool.join()
print(results)


myClass = someParams( 5,5,3)
myPool = mp.Pool(number_of_Processors)  
results = myPool.map(myClass.getLHC, [i for i in range(number_of_Processors)])  
myPool.close()  
myPool.join()
print(results)

myClass = someParams( 5,5,3)
myPool = mp.Pool(number_of_Processors)  
results = myPool.map(myClass.getLHC, [i for i in range(number_of_Processors)])  
myPool.close()  
myPool.join()
print(results)

myClass = someParams( 5,5,2)
myPool = mp.Pool(number_of_Processors)  
results = myPool.map(myClass.getLHC, [i for i in range(number_of_Processors)])  
myPool.close()  
myPool.join()
print(results)


myClass = someParams( 1000,1000,3)
myPool = mp.Pool(number_of_Processors)  
results = myPool.map(myClass.getLHC, [i for i in range(number_of_Processors)])  
myPool.close()  
myPool.join()
print(results)


