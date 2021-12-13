import numpy as np

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

#xlen = 11
#ylen = 15

xlen = 1311
ylen = 895

arr = np.zeros((ylen, xlen), dtype=np.uint)
folds = []

for line in lines:
    spl = line.split()

    if len(spl) == 3:
        spl = spl[2].split("=")
        spl = (spl[0], int(spl[1]))
        folds.append(spl)
    elif len(spl) == 1:
        spl = tuple(map(int, spl[0].split(",")))
        print(spl)
        arr[spl[1], spl[0]] = 1

print(arr)

for fold in folds:
    print(fold)
    
    if fold[0] == "y":
        fst = arr[:fold[1], :]
        snd = np.flipud(arr[fold[1]+1:,:])
    else:
        fst = arr[:, :fold[1]]
        snd = np.fliplr(arr[:, fold[1]+1:])


    #print (fst)
    #print ("-----------")
    #print (snd)

    arr = fst | snd
    #print (arr)
    #print("\n")

for i in arr:
    for j in i:
        if j:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()