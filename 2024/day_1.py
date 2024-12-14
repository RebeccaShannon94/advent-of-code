import pandas as pd

input_file = "data/input_day_1.csv"
data = pd.read_csv(input_file, header=None, sep="\s+")

lst_1 = sorted(data[0].tolist())
lst_2 = sorted(data[1].tolist())

dif_count = 0
similarity_score = 0

for i, j in zip(lst_1, lst_2):
    dif_count += abs(i - j)
    similarity_score += i * sum(n == i for n in lst_2)

print(f"dif count: {dif_count}")
print(f"similarity score: {similarity_score}")
