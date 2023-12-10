import re
import argparse

input_file = "test_input.txt"  # Test
input_file = "input.txt"

nums = [str(x) for x in range(10)]
normals = set(nums + ["."])
parser = argparse.ArgumentParser()
parser.add_argument(
    "-log",
    "--loglevel",
    default="warning",
    help="Provide logging level. Example --loglevel debug, default=warning",
)

args = parser.parse_args()


def lprint(s="\n", end="\n"):
    global args
    if args.loglevel.upper() == "DEBUG":
        print(s, end=end)
    return


gear_dict = {}


def find_gears(grid, gears):
    global gear_dict
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "*":
                gear_dict[f"{x}-{y}"] = []
                gears[x][y] = 1
    return gears


def find_symbols(grid, symbol_grid):
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char not in normals:
                symbol_grid[x][y] = 1
    return symbol_grid


def check_limits(y, grid):
    if y >= 0 and y < len(grid):
        return True
    return False


def check_access(x1, x2, y, symbol_grid):
    if x1 < 0:
        x1 = 0
    if x2 < 0:
        x2 = 0
    # check y-1, y, y+1
    # print(f"will check x1: {x1} x2: {x2} y: {y}")
    # print(symbol_grid[y-1:y+1])
    if check_limits(y - 1, symbol_grid) and sum(symbol_grid[y - 1][x1:x2]) > 0:
        # print(symbol_grid[y-1][x1:x2])
        return True
    elif check_limits(y, symbol_grid) and sum(symbol_grid[y][x1:x2]) > 0:
        # print(symbol_grid[y][x1:x2])
        return True
    elif check_limits(y + 1, symbol_grid) and sum(symbol_grid[y + 1][x1:x2]) > 0:
        # print(symbol_grid[y+1][x1:x2])
        return True

    return False


def get_locs(x1, x2, grid_line):
    for i, b in enumerate(grid_line):
        if i >= x1 and i <= x2 and b:
            yield i


def check_access_loc(x1, x2, y, gear_grid, number):
    if x1 < 0:
        x1 = 0
    if x2 < 0:
        x2 = 0

    if check_limits(y - 1, gear_grid) and sum(gear_grid[y - 1][x1 : x2 + 1]) > 0:
        return [f"{y-1}-{b}" for b in get_locs(x1, x2, gear_grid[y - 1])]
    elif check_limits(y, gear_grid) and sum(gear_grid[y][x1 : x2 + 1]) > 0:
        return [f"{y}-{b}" for b in get_locs(x1, x2, gear_grid[y])]
    elif check_limits(y + 1, gear_grid) and sum(gear_grid[y + 1][x1 : x2 + 1]) > 0:
        return [f"{y+1}-{b}" for b in get_locs(x1, x2, gear_grid[y + 1])]

    return False


result = 0


def solve_gears(grid, gear_grid):
    global result, gear_dict
    for y, line in enumerate(grid):
        matches = re.finditer(r"\d+", line)
        lprint("\n\n")
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            number = match.group()
            # Seek for symbol access;
            # in current line; start_index-1:end_index+2
            x1 = start_index - 1
            x2 = end_index
            r = check_access_loc(x1, x2, y, gear_grid, number)
            if r:
                for x in r:
                    lprint(f"will add {number} to {x}")
                    gear_dict[x].append(number)
                lprint(f"{number} has access")
            lprint(f"Number: {number}, Start Index: {x1}, End Index: {x2}")


def solve(grid, symbol_grid):
    global result
    for y, line in enumerate(grid):
        matches = re.finditer(r"\d+", line)
        # for m in matches:
        #    lprint(f"{m.group()} -", end='')
        lprint("\n\n")
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            number = match.group()
            # Seek for symbol access;
            # in current line; start_index-1:end_index+2
            x1 = start_index - 1
            x2 = end_index + 1
            if check_access(x1, x2, y, symbol_grid):
                result += int(number)
                lprint(f"{number} has access")
            # lprint(f"Number: {number}, Start Index: {start_index}, End Index: {end_index - 1}")


grid = []

with open(input_file, "r") as file:
    for line in file:
        grid.append(line.strip("\n"))

symbol_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
symbol_grid = find_symbols(grid, symbol_grid)
gears = [[0] * len(grid[0]) for _ in range(len(grid))]
gears = find_gears(grid, gears)

# solve(grid, symbol_grid)
solve_gears(grid, gears)
# print(result)
r = 0
# calculate result
for k, v in gear_dict.items():
    if len(v) == 2:
        r += int(v[0]) * int(v[1])

print(r)
