# %%

dados = ['téo', 'calvo', 30] # lista

nome = dados[0]

dados = {"nome": "Téo", "sobrenome": "Calvo", "idade":31}

nome = dados["nome"]
print(nome)

# %%

dados = {
    "nome": "Téo",
    "sobrenome": "Calvo",
    "idade": 31,
    "ex": ["Nah", "Josefina", "Elaine"],
    "filhos": [ {"nome": "Maria", "idade": 2}, {"nome": "Raul", "idade": 1}]
}

nome = dados["nome"]
print(nome)

print(dados["filhos"][0]["idade"])
# %%

dados.keys()

# %%
dados.values()


# %%
dados.items()