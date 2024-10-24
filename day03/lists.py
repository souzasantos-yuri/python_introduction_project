# %%

my_empty_list = []

print(my_empty_list)
# %%

my_list = ["Téo", "Calvo", 31, 1.82]
print(my_list)
# %%

my_list[0]
# %%

my_list[3]
# %%

my_list[len(my_list)-2]
# %%

my_list[-2]
# %%

my_list[100]


# %%
my_list[0:2]
# %%

my_list[0:-1]
# %%

my_list[0: int(len(my_list)/2)]
# %%

my_list[:2]
# %%

my_list[::-1]
# %%

my_list[::-2]
# %%

my_list[::2]
# %%

notas = []
nota = 7.75

notas.append(nota)
# %%
print(notas)
# %%

notas.append(10)
print(notas)
# %%
notas.extend([5.75, 6.24])
# %%
print(notas)
# %%
notas = notas + [10, 9.25]
# %%
print(notas)
# %%

nome = 'teo'
nome_alto = nome.upper()
print(nome_alto)
print(nome)
# %%

nomes = ['teo', 'maria', 'nah']
for i in nomes:
    print(i.title())

nomes.extend(['jose', 'lila'])
# %%

dados = ['Teo', 'Calvo', 31, ['Nah', 'Josefina', 'Elaina'], ['Maria']]

dados[3][-1]

# %%

dados[-1][0][0]