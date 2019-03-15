#
# get and set process affinity
#

import psutil

print(psutil.cpu_count(logical=False))

p = psutil.Process()
print(dir(p))
print(p.cpu_affinity())  # not defined on mac

p.cpu_affinity([0, 1])
print(p.cpu_affinity())  # not defined on mac

p.cpu_affinity([])
print(p.cpu_affinity())  # not defined on mac


