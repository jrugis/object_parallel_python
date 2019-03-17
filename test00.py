#
# run time test
#
#  mac:         3.4
#  nectar:      22
#  nesi build:
#  nesi run:

import time
import numpy as np

# execution timer
start = time.time()

incr = np.double(0.1)
x = incr
for i in range(1000000):
    k = np.log(x)
    l = np.sin(x)
    m = np.cos(x)
    x += incr
    
# execution timer
end = time.time()
print(end - start)

