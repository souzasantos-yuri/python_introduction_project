# 1
# 10.0
# -5
# -7.54

sum = 2 + 2

#Booleans
True
False

condition = 12 > 18

if condition:
    print("This is true")
else:
    print("This will never happen")

age = int(input("Tell me your age: "))
drivers_license = input("Do you have a license? ")

if age > 18 and drivers_license == "yes":
    print("Keep going")

else:
    print("You are arrested!!!")

condicao = age >= 18 and drivers_license == "sim"
print(condicao)


print("True and True =", bool(1 * 1))
print("False and True =", bool(0 * 1))
print("True and False =", bool(1 * 0))
print("False and False =", bool(0 * 0))

print("True and True =", bool(1 + 1))
print("False and True =", bool(0 + 1))
print("True and False =", bool(1 + 0))
print("False and False =", bool(0 + 0))
