
con_1 = ['M','M','S','S']
con_2 = ['S','S','M','M']
con_3 = ['M','S','M','S']
con_4 = ['S','M','S','M']

memory_text = open('data/input_day_4.txt', 'r').read().splitlines()

def xmas_check(input_lst: list, condition: list):

    xmas_count = 0

    for row in list(range(0,len(input_lst)-2,1)):

        for col in list(range(0,len(input_lst[0])-2,1)):

            if input_lst[row][col] == condition[0] and \
                input_lst[row][col+2] == condition[1] and \
                    input_lst[row+1][col+1] == 'A' and \
                        input_lst[row+2][col] == condition[2] and \
                            input_lst[row+2][col+2] == condition[3]:
                xmas_count += 1
    
    return xmas_count

xmas_count_sum = 0

for condition in [con_1,con_2,con_3,con_4]:

    xmas_count_sum += xmas_check(memory_text,condition)

print(f'Conditions are met {xmas_count_sum} times')

