from bitstring import BitArray

inputfile = open('input.txt', 'r')
lines1 = inputfile.readlines()
lines2 = lines1.copy()

count = [0,0,0,0,0,0,0,0,0,0,0,0]
bitfilter = [0,0,0,0,0,0,0,0,0,0,0,0]

idx = 0
while len(lines1) != 1:
    for line in lines1:
        count[idx] = count[idx] + int(line[idx])


    if count[idx] >= len(lines1)/2:
        bitfilter[idx] = 1
    else:
        bitfilter[idx] = 0


    print("idx", idx, "count[idx]",count[idx], "lines1 length", len(lines1), "bitfilter[idx]", bitfilter[idx])
    lines1 = [line for line in lines1 if int(line[idx]) == bitfilter[idx]]

    idx = idx + 1

print ("oxygen", lines1[0][:-1], "dec", int(lines1[0],2))

count = [0,0,0,0,0,0,0,0,0,0,0,0]
bitfilter = [0,0,0,0,0,0,0,0,0,0,0,0]
idx=0
while len(lines2) != 1:
    for line in lines2:
        count[idx] = count[idx] + int(line[idx])


    if count[idx] < len(lines2)/2:
        bitfilter[idx] = 1
    else:
        bitfilter[idx] = 0


    print("idx", idx, "count[idx]",count[idx], "lines2 length", len(lines2), "bitfilter[idx]", bitfilter[idx])
    lines2 = [line for line in lines2 if int(line[idx]) == bitfilter[idx]]

    idx = idx + 1

print ("co2", lines2[0][:-1], "dec", int(lines2[0],2))

inputfile.close()

print ("multiply", int(lines2[0],2) * int(lines1[0],2))