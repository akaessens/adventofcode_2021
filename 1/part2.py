inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
 
count = 0
prev = [ 1e10, 1e10 , 1e10 ]

for line in lines:
    curr = int(line)

    sum_curr = curr + prev[0] + prev[1]
    sum_prev = sum(prev)

    if sum_curr > sum_prev:
        count = count+1

    prev.pop() # remove last value
    prev.insert(0, curr) # add curr as prev[0]

print("Count", count)