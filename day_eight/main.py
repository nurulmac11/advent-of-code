from collections import defaultdict, OrderedDict
import functools

file_path = "test_input.txt"
file_path = "input.txt"

instrs = ""
mapping = {}
head_pivot = ""
starters = []
endings = set()

def parse_file(file_path):
    global instrs, mapping, head_pivot, starters
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i == 0:
                instrs = line.strip()
            elif i > 1:
                # AAA = (BBB, CCC)
                twoparts = line.strip().split('=')
                key = twoparts[0].strip()
                values = twoparts[1][2:-1].split(', ')
                if i == 2:
                    head_pivot = key
                mapping[key] = values
                if key[-1] == 'A':
                    starters.append(key)
                if key[-1] == 'Z':
                    endings.add(key)
def ending_check(pivots):
    global endings
    for pivot in pivots:
        if pivot not in endings:
            return False
    return True

def process(pivots):
    global mapping, instrs
    step = 0
    current_i = 0
    while not ending_check(pivots):
        current_i %= len(instrs)
        new_pivots = []
        currents = [mapping[pivot] for pivot in pivots]
        c = instrs[current_i]
        if c == 'R':
            new_pivots = [current[1] for current in currents]
        elif c == 'L':
            new_pivots = [current[0] for current in currents]
        pivots = new_pivots
        step += 1
        current_i += 1
        print(step, pivots)
    return step

parse_file(file_path)
print(starters)
print(endings)
per = []
import math
for s in starters:
    r = process([s])
    per.append(r)
print(per)
print(math.lcm(*per))