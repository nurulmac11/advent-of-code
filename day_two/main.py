import re


#input_file = 'input_test.txt' # Test
input_file = 'input.txt'
   
# limits:
#  12 red cubes, 13 green cubes, and 14 blue cubes
r_limit, g_limit, b_limit = 12, 13, 14

def count_balls(input_str):
    colors = {}
    input_str = input_str.strip()
    items = input_str.split(', ')
    
    for item in items:
        quantity, color = item.split(' ')
        quantity = int(quantity)
        
        if color in colors:
            colors[color] += quantity
        else:
            colors[color] = quantity
    
    return colors

def check_limits(game):
    r, g, b = game.get_max_of_sets()
    if r > r_limit or g > g_limit or b > b_limit:
        return False
    return True

def get_power(game):
    r, g, b = game.get_max_of_sets()
    r = r if r else 1
    g = g if g else 1
    b = b if b else 1
    return r*g*b

class Set:

    def __init__(self, set_input):
        self.r = set_input.get('red', 0)
        self.g = set_input.get('green', 0)
        self.b = set_input.get('blue', 0)

class Game:

    def __init__(self, index, sets):
        self.index = index
        self.sets = sets
    
    def get_max_of_sets(self):
        r, g, b = 0, 0, 0
        for se in self.sets:
            r = max(r, se.r)
            g = max(g, se.g)
            b = max(b, se.b)
        return r, g, b

    def __str__(self):
        print(f"GAME {self.index}")
        print("SETS")
        for se in self.sets:
            print(f"R: {se.r} G: {se.g} B: {se.b}")
        return ""

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
'''
game_objects = []
with open(input_file, 'r') as file:
    for line in file:
        # line = game
        # ; set
        game, set_split = line.split(':')
        game_index = int(game.split(' ')[1])
        sets = set_split.split(';')
        print(line)
        set_objects = []
        for set_input in sets:
            set_objects.append(Set(count_balls(set_input)))
        game_objects.append(Game(game_index, set_objects))

result = 0
for game in game_objects:
    result += get_power(game)

print(result)

