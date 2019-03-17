#
# run time test
#
#  mac:         3.4
#  nectar:      22 (4.5)
#  nesi build:  4.3
#  nesi run n4: 4.3
#  nesi run n8: 4.3 
    
import time
import numpy as np

# for loop
def A():
    incr = np.double(0.1)
    x = incr
    for i in range(1000000):
        k = np.log(x)
        l = np.sin(x)
        m = np.cos(x)
        x += incr

# numpy iterate
def B():
    x = np.arange(start=0.1, stop=10000.0, step=0.1, dtype="double")
    for t in x:
        k = np.log(t)
        l = np.sin(t)
        m = np.cos(t)
    
# numpy array
def C():
    x = np.arange(start=0.1, stop=10000.0, step=0.1, dtype="double")
    k = np.log(x)
    l = np.sin(x)
    m = np.cos(x)
    
start = time.time()
A()
end = time.time()
print(end - start)

start = time.time()
B()
end = time.time()
print(end - start)

start = time.time()
end = time.time()
C()
print(end - start)
