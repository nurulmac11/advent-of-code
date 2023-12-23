file_path = "test_input.txt"
file_path = "input.txt"


def parse_file(file_path):
    data = {'Time': [], 'Distance': []}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 1:
                label = parts[0].rstrip(':')
                values = [int(val) for val in parts[1:]]
                data[label].extend(values)
    td = []
    longtime = ""
    longdistance = ""
    for time in data['Time']:
        longtime += str(time)
    for distance in data['Distance']:
        longdistance += str(distance)
    return [[int(longtime), int(longdistance)]]

def runs(time, record):
    # time:7, record: 9
    '''
    t=7
    x: 0->7
    (7-x) * x
    7x - x^2
    '''
    records = 0
    for i in range(time):
        lap = time * i - (i*i)
        if lap > record:
            records += 1
    return records

td_list = parse_file(file_path)
result = 1
print(td_list)

for time, record in td_list:
    r = runs(time, record)
    print(f"record count for {time} is {r}")
    result *= r
print(result)