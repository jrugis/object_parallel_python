#
# run time test
#

import time
import math as m
from multiprocessing import Process, Pipe

# execution timer
start = time.time()

for i in range(10000000):
    k = m.log(i+1)
    l = m.sin(i)
    l = m.cos(i)

# execution timer
end = time.time()
print(end - start)

