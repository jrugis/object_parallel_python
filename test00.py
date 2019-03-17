#
# run time test
#

import time
import numpy as np
from multiprocessing import Process, Pipe

# execution timer
start = time.time()

incr = np.float32(0.1)
x = incr
for i in range(1000000):
    k = np.log(x)
    l = np.sin(x)
    m = np.cos(x)
    x += incr
    
# execution timer
end = time.time()
print(end - start)

