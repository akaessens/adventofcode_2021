import numpy as np
import statistics

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()

symbols = [
    ("(", ")", 3, 1),
    ("{", "}", 1197, 3),
    ("<", ">", 25137, 4),
    ("[", "]", 57, 2)
]


def get_error(illegal):
    for pair in symbols:
        if pair[1] == illegal:
            return pair[2]


def get_completion(opening):
    for pair in symbols:
        if pair[0] == opening:
            return pair[3]


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

        # closing last open
        if open_chars and curr_char == closing(open_chars[-1]):
            pos += 1
            open_chars.pop(-1)
        elif closing(curr_char):  # open another
            pos += 1
            open_chars.append(curr_char)
        else:
            err = get_error(curr_char)
            #print ("Error at pos", pos, "expected", closing(open_chars[-1]), "but got", curr_char, "error", err)
            return 0

    return open_chars


def repair(open_chars):
    score = 0
    app = []
    for opening in reversed(open_chars):
        app.append(closing(opening))
        rep = get_completion(opening)
        score *= 5
        score += rep

    #print (app)
    return score


total_score = []
for line in lines:
    # print("-----------------------------------")
    # print(line)
    open_chars = syntax_check(line)

    if open_chars:

        #print ("remaining open_chars", open_chars)
        total_score.append(repair(open_chars))

print(statistics.median(total_score))
