import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(DIRECTORY, "input.txt")
DEFAULT_TARGET = 2020

# Part 1
with open(INPUT_FILE) as f:
    NUMBERS = [int(n) for n in f]

def find_pair(numbers=NUMBERS, target=DEFAULT_TARGET):
    n1 = None
    n2 = None
    seen_values = set()
    for num in numbers:
        n1 = num
        n2 = target - num

        if n2 in seen_values:
            return n1, n2
        seen_values.add(n1)

    return None, None

def part_one():
    a, b = find_pair()
    return a * b if a and b else None

def part_two():
    for n in NUMBERS:
        sub_target = DEFAULT_TARGET - n
        n2, n3 = find_pair(target=sub_target)
        if n2 and n3:
            return n * n2 * n3

    return None

print 'Part 1: ', part_one()
print 'Part 2: ', part_two()
