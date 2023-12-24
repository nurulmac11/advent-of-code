from collections import defaultdict, OrderedDict
import functools

file_path = "test_input.txt"
file_path = "input.txt"

num_list = []
def parse_file(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            nums = line.strip().split(' ')
            nums = list(map(int, nums))
            num_list.append(nums)


def parse_down(nums):
    diffs = []
    for i in range(0, len(nums)-1):
        diffs.append(nums[i+1] - nums[i])
    last = diffs[0]
    is_same = True
    for d in diffs:
        if d != last:
            is_same = False
        last = d
    if is_same:
        return last
    else:
        return diffs[0] - parse_down(diffs)

parse_file(file_path)
results = []
for num in num_list:
    print(num)
    r = parse_down(num)
    results.append(num[0] - r)
    print(r)
    print('\n')
print(sum(results))