# %%

qty = int(input("Quantos anos você tem?"))

count = 1

while count <= qty:
    print("Idade")
    count += 1 # count = count + 1

# %%

while True:

    password = input("Enter any password: ")

    if password == "burger":
        break

    elif password == "rice":
        print("almost there")
        continue

    print("blablabla")
    print("blablablaaaaaaaaa")
    print("blaaaaaaaaaaaaablabla")

print("Exited the infinity loop")
# %%

counter = 1
while counter <= 15: 
    if counter % 2 == 0:
        print(counter)
        
    counter += 1