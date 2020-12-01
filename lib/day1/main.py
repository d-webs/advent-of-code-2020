import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(DIRECTORY, "input.txt")

# Part 1
with open(INPUT_FILE) as f:
    target = 2020
    seen_values = set()

    num_as_int = None
    inverse = None
    for num in f:
        num_as_int = int(num)
        seen_values.add(num_as_int)
        inverse = target - num_as_int

        if inverse in seen_values:
            break

    print 'Part 1:',  num_as_int * inverse
