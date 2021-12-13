from bitstring import BitArray

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

count = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
    array = [int(char) for char in line[:-1]]

    for idx in range(len(count)):
        count[idx] = count[idx] + array[idx]

inputfile.close()

for idx in range(len(count)):
    if count[idx] >= len(lines)/2:
        gamma[idx] = 1
    else:
        epsilon[idx] = 1

print("count", count)
print("gamma", gamma)
print("epsilon", epsilon)

gamma_dec = BitArray(gamma).uint
epsilon_dec = BitArray(epsilon).uint

print( "multiplied", gamma_dec*epsilon_dec)