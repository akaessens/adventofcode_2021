import numpy as np

crabs = np.loadtxt("testinput.txt", dtype='int', delimiter=',')

positions = max(crabs)
fuel = np.zeros(positions, dtype='int')

for step in range(positions):
    for crab in crabs:
        d = abs(crab-step)
        fuel[step] += (d**2 + d) / 2 # little gauss

print(min(fuel))
