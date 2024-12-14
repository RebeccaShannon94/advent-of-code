import re

file = open('data/input_day_3.txt', 'r')
text = file.read()

split_lst = text.split("do()")
enable_lst = []
for item in split_lst:
    if "don't()" in item:
        enable_lst.append(item.split("don't()")[0])
    else:
        enable_lst.append(item)

sum = 0
for item in enable_lst:
    memory_keep = re.findall('mul\(\d*\,\d*\)', item)
    for i in list(range(0,len(memory_keep),1)):
        values = re.findall('(\d+)', memory_keep[i])
        sum += int(values[0]) * int(values[1])

print(f'Sum of values: {sum}')