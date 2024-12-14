import re

input_file = open('data/input_day_3.txt', 'r')
memory_text = input_file.read()
memory_keep = re.findall('mul\(\d*\,\d*\)', memory_text)

sum = 0

for i in list(range(0,len(memory_keep),1)):
    values = re.findall('(\d+)', memory_keep[i])
    sum += int(values[0]) * int(values[1])

print(f'Sum of values: {sum}')
