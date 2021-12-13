import numpy as np

crabs = np.loadtxt("input.txt", dtype='int', delimiter=',')

positions = max(crabs)
fuel = np.zeros(positions, dtype='int')

for step in range(positions):
    for crab in crabs:
        fuel[step] += abs(crab-step)

print(min(fuel))
