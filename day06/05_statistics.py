def sum(a:float, b:float, *args)->float:
    values = [a,b] + list(args)
    return sum(values)

def average(a:float, b:float, *args)->float:
    return sum(a,b, *args) / (len(args)+2)

a = float(input("enter the A value: "))
b = float(input("enter the B value: "))
c = float(input("enter the C value: "))

print(f"Average: {average(a,b,c)}")