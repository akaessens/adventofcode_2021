inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
 
count = 0
pos = [0, 0]
aim = 0

for line in lines:

    direction = line.split()
    length = + int(direction[1])

    if (direction[0] == "forward"):
        pos[0] = pos[0] + length
        pos[1] = pos[1] + aim*length
    elif (direction[0] == "up"):
        aim = aim - length
    elif (direction[0] == "down"):
        aim = aim + length

inputfile.close()

print("Pos", pos, "multiplied", pos[0]*pos[1])