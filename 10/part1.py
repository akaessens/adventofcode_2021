import numpy as np

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

symbols = [
    ("(", ")", 3),
    ("{", "}", 1197),
    ("<", ">", 25137),
    ("[", "]", 57)
]

def get_error(illegal):
    for pair in symbols:
        if pair[1] == illegal:
            return pair[2]

def closing(opening):
    for pair in symbols:
        if pair[0] == opening:
            return pair[1]
    return 0

def syntax_check(line):
    open_chars = []
    pos = 0

    while pos != len(line):
        if line[pos] == "\n":
            break

        curr_char = line[pos]

        #print ("pos", pos, "curr_char", curr_char)

        if open_chars and curr_char == closing(open_chars[-1]): # closing last open
            pos += 1
            open_chars.pop(-1)
        elif closing(curr_char): # open another
            pos += 1
            open_chars.append(curr_char)
        else:
            err = get_error(curr_char)
            print ("Error at pos", pos, "expected", closing(open_chars[-1]), "but got", curr_char, "error", err)
            print ("remaining open_chars", open_chars)
            return err

    print ("remaining open_chars", open_chars)
    return 0

sum_err = 0
for line in lines:
    print("-----------------------------------")
    print(line)
    err = syntax_check(line)
    sum_err += err

print ("Sum", sum_err)
