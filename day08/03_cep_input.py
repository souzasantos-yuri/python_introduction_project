import requests
cep = input("enter the zip code: ")

url = "https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url.format(cep=cep))

data = dict()

if response.status_code == 200:
    data = response.json()

for key, value in data.items():
    print(f"{key} => {value}" )