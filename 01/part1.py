inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
 
count = 0
prev = 1e10

for line in lines:
    curr = int(line)

    if curr > prev:
        count = count + 1

    prev = curr

print("Count", count)