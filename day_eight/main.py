from collections import defaultdict, OrderedDict
import functools

file_path = "test_input.txt"
file_path = "input.txt"

instrs = ""
mapping = {}
head_pivot = ""
def parse_file(file_path):
    global instrs, mapping, head_pivot
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
    
def process(pivot):
    global mapping, instrs
    step = 0
    current_i = 0
    while pivot != 'ZZZ':
        current_i %= len(instrs)
        current = mapping[pivot]
        c = instrs[current_i]
        if c == 'R':
            pivot = current[1]
        elif c == 'L':
            pivot = current[0]
        step += 1
        current_i += 1
    return step

parse_file(file_path)
r = process(head_pivot)
print(r)