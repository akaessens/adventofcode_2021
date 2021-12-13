import numpy as np
import re



def find_bingo(array):
    for i in range(len(array)):
        if sum(array[:,i]) == len(array):
            return ("row", i)
        if sum(array[i,:]) == len(array):
            return ("col", i)

    return 0

def result(board, array, number):
    unmarked_sum = 0
    for ix,iy in np.ndindex(array.shape):
        print ("ix", ix, "iy", iy, "array[ix,iy] ", array)
        if array[ix,iy] == 0:
            unmarked_sum += board[ix,iy]

    print ("unmarked_sum", unmarked_sum, "number", number, "multiply", unmarked_sum * number)
    
    return 0

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

draw = list(map(int, re.findall('\d+', lines[0])))
lines.pop(0)
lines.pop(0)

boards = np.zeros((100,5,5))
select = np.zeros((100,5,5))
winners = np.zeros(100)

board_idx = 0
row_idx = 0
for line in lines:
    if line == "\n":
        board_idx += 1
        row_idx = 0
        continue

    row = list(map(int, re.findall('\d+', line)))
    boards[board_idx, row_idx] = row
    row_idx += 1

inputfile.close()

for number in draw:
    print("number", number)

    for board_idx in range(len(boards)):
        idx = np.where(boards[board_idx]==number)

        if (idx[0].size):
            select[board_idx][idx] = 1

        check = find_bingo((select[board_idx]))
        if type(check) != int:
            winners[board_idx] = 1
            if sum(winners) == len(winners): # last one won
                result(boards[board_idx], select[board_idx], number)
                exit(0)


