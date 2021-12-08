import numpy as np
import itertools


def match_pattern(in_out):
    numbers = dict()
    signals = dict()

    for word in in_out[0].split():
        if len(word) == 2:
            numbers.update({1: set(word)})
        elif len(word) == 3:
            numbers.update({7: set(word)})
        elif len(word) == 4:
            numbers.update({4: set(word)})
        elif len(word) == 7:
            numbers.update({8: set(word)})

    for word in in_out[0].split():
        if len(word) == 6: # all numbers with 6 segments
            missing = next(iter(numbers.get(8) - set(word)))
            if missing in numbers.get(1): # found 6
                numbers.update({6: set(word)})
                signals.update({"c": set(missing)})

    f = numbers.get(1) - signals.get("c")
    signals.update({"f": set(f)})
    a = numbers.get(7) - signals.get("c") - signals.get("f")
    signals.update({"a": set(a)})

    for word in in_out[0].split():
        if len(word) == 5: # all numbers with 5 segments
            if next(iter(signals.get("c"))) not in word: # found 5
                numbers.update({5: set(word)})
                e = numbers.get(8)-numbers.get(5)-signals.get("c")
                signals.update({"e": set(e)})
                break

    g = numbers.get(8) - numbers.get(7) - numbers.get(4) - signals.get("e")
    signals.update({"g": set(g)})

    for word in in_out[0].split():
        if len(word) == 6: # all numbers with 6 segments
            if set(word) != numbers.get(6): # not number 6
                if next(iter(signals.get("e"))) in word: # found 0
                    numbers.update({0: set(word)})
                    d = numbers.get(8)-numbers.get(0)
                    signals.update({"d": set(d)})
                    break

    
    b = numbers.get(4) - numbers.get(1) - signals.get("d")
    signals.update({"b": set(b)})

    two =   numbers.get(8) - signals.get("b") - signals.get("f")
    three = numbers.get(8) - signals.get("b") - signals.get("e")
    nine =  numbers.get(8) - signals.get("e")

    numbers.update({2: set(two)})
    numbers.update({3: set(three)})
    numbers.update({9: set(nine)})

    return numbers

with open('input.txt', 'r') as inputfile:
    lines = inputfile.readlines()

result = 0
for line in lines:
    in_out = line.split("|")
    mapping = match_pattern(in_out)

    arr = []
    for out in in_out[1].split():

        for nr in range(10):
            if mapping.get(nr) == set(out):
                arr.append(str(nr))

    value = int("".join(arr))
    print (value)
    result += value

print("Result", result)
