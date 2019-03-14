#
# get and set process affinity
#

import psutil

print(psutil.cpu_count())

p = psutil.Process()
print(p.cpu_affinity())

p.cpu_affinity([0, 1])
print(p.cpu_affinity())

p.cpu_affinity([])
print(p.cpu_affinity())


