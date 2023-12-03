import re


#input_file = 'input_test.txt' # Test
input_file = 'input.txt'
digit_map = [
        ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), 
        ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'),
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')]

def get_number(line):
    nums = ""
    nums_nonorder = []
    for digit in digit_map:
        # get all matches
        index_list = [m.start() for m in re.finditer(f'(?={digit[0]})', line)]
        if index_list:
            for index in index_list:
                nums_nonorder.append([digit[1], index, len(digit[0])])
    nums_checked = sorted(nums_nonorder, key = lambda x: x[1])
    
    if not nums_checked:
        return 0 

    num = nums_checked[0][0] + nums_checked[-1][0]

    return int(num)
    

total_value = 0 
with open(input_file, 'r') as file:
    for line in file:
        total_value += get_number(line)

print(total_value)
