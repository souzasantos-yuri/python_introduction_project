# %%

x = []

for i in range(1,101):
    x.append(i)

x

# %%

y = [i for i in range(1,101)]
y

# %%

def even(x):
    return x % 2 == 0

z = [even(i) for i in range(1,101)]
z

# %%

w = [i for i in range(1,101) if even(i)]
w