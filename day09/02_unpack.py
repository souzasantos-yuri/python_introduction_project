# %%

A = 1
B = 5

print(A)
print(B)

# %%

C = A
A = B
B = C
print(A)
print(B)

# %%

B, A = A, B

# %%

a, b = "teo", [1,2,4]
print(a,b)

# %%

a, b, *resto = 1, 2, 3, 4,5,5,6,56,56,5,6
print(a,b, resto)

# %%

def soma(a, *args):
    total = a + sum(args)
    return total


soma(1,2,4,7)

# %%

def soma_quatro(a,b,c,d):
    return a+b+c+d


values = [1,2,3,4]
soma_quatro(*values)

# %%
soma(*values)

# %%

dados = {"nome": "teo", "sobrenome":"calvo"}
for i, j in dados.items():
    print(i,j)