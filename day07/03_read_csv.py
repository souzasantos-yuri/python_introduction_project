# %% 

file = "data.csv"

with open(file) as open_file:
    data = open_file.readlines()

for i in data:
    print(i)

# %%

dice = dict()

keys = data[0].strip("\n").split(";")

for k in keys:
    dice[k] = []

# %%

for d in data[1:]:
    values = d.strip("\n").split(";")
    for i in range(0, len(values)):
        dice[keys[i]].append(values[i])

dice

# %%

ages = []

for i in dice["age"]:
    ages.append(int(i))

average = sum(ages) / len(ages)
average
