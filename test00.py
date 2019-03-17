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
start = time.time()
incr = np.double(0.1)
x = incr
for i in range(1000000):
    k = np.log(x)
    l = np.sin(x)
    m = np.cos(x)
    x += incr
end = time.time()
print(end - start)

# numpy array
start = time.time()
x = np.arange(start=0.1, stop=10000.0, step=0.1, dtype="double")
k = np.log(x)
l = np.sin(x)
m = np.cos(x)
end = time.time()
print(end - start)

# numpy iterate
start = time.time()
for t in x:
    k = np.log(t)
    l = np.sin(t)
    m = np.cos(t)
end = time.time()
print(end - start)

