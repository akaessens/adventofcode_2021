with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()

fish = list(map(int, lines[0].split(",")))

days = 80

for day in range(1,days+1):
    for idx in range(len(fish)):
        if fish[idx] == 0:
            fish[idx] = 6
            fish.append(8)
        else:
            fish[idx] -= 1

    #print("Day {:2,}".format(day), fish)

print("Sum of", len(fish))