# %%

import requests
import json
from tqdm import tqdm
import pandas as pd

# %%

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "19060100",
    "58038200",
]

url = "https://viacep.com.br/ws/{cep}/json/"
data = []

for i in tqdm(ceps):
    response = requests.get(url.format(cep=i))
    if response.status_code = 200:
        data.append(response.json())
data

# %%
# 
dataset = pd.DataFrame(data)
dataset.to_csv("ceps.csv", sep=";")

# %%

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(data, open_file, ensure_ascii=False, indent=4)