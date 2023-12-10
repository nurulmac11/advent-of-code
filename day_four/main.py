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
    return ""


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

wins = {}


def parser(line):
    l1, l2 = line.split(":")[1].split("|")
    l1, l2 = l1.strip(), l2.strip()
    winners = l1.split(" ")
    played = l2.split(" ")
    winners_set = set()
    played_int = []
    for x in winners:
        if x:
            winners_set.add(int(x))
    for x in played:
        if x:
            played_int.append(int(x))
    r = -1
    for p in played_int:
        if p in winners_set:
            r += 1
    return 2**r if r >= 0 else 0


points = 0
with open(input_file, "r") as file:
    for line in file:
        points += parser(line)

print(points)


# part 2
def parser2(line):
    l1, l2 = line.split(":")[1].split("|")
    l1, l2 = l1.strip(), l2.strip()
    winners = l1.split(" ")
    played = l2.split(" ")
    winners_set = set()
    played_int = []
    for x in winners:
        if x:
            winners_set.add(int(x))
    for x in played:
        if x:
            played_int.append(int(x))
    r = 0
    for p in played_int:
        if p in winners_set:
            r += 1
    return r


line_wins = {}
with open(input_file, "r") as file:
    for i, line in enumerate(file):
        line_wins[i] = parser2(line)


def total_cards(board, pivot):
    if board[pivot] > 0:
        r = board[pivot]
        for y in range(pivot + 1, pivot + board[pivot] + 1):
            # print(pivot, r, y, pivot + board[pivot])
            r += total_cards(board, y)
        return r
    return 0


all_r = 0
for i in range(len(line_wins)):
    r = total_cards(line_wins, i)
    all_r += r
print(all_r + len(line_wins))
