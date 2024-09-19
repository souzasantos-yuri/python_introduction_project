# Create a program that receives a number in seconds and convert it to DATETIME

# input: 556
# output: 0:9:16
# input: 140153
# output: 38:55:53

seconds = int(input("Tell me the time in seconds: "))

hours = seconds // (60 * 60) # // is a floor division
seconds = seconds % (60 * 60) # % gets the rest of the division

minutes = seconds // 60
seconds = seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")