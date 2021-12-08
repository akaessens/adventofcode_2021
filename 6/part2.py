from joblib import Parallel, delayed
import numpy as np


def process(fish, day):
    for idx in range(len(fish)):
        if fish[idx] == 0:
            fish[idx] = 6
            fish = np.append(fish,8)
        else:
            fish[idx] -= 1

    #print("Day {:2,}".format(day), fish)
    return fish

with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()

fish = np.array(list(map(int, lines[0].split(","))))

days = 256
jobs = 8
for day in range(1,days+1):

    chunks = np.array_split(fish, jobs)

    results = Parallel(n_jobs=jobs)(delayed(process)(chunk, day) for chunk in chunks)

    fish = np.concatenate(results)

    print("Day {:2,}".format(day), fish)

print("Sum of", len(fish))
