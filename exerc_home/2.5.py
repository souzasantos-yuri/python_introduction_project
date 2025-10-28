# Consider the list: [120, 'Python', 120.01, 'asw', False, [10, 20]]
#Create a program that returns the following information:
#Element at position -1 of the list
#Element at the first position of the list
#The last character of the second element of the list

my_list = [120, 'Python', 120.01, 'asw', False, [10, 20]]

print(f"Position -1: {my_list[-1]}")
print(f"First position: {my_list[0]}")
print(f"The last character of the second element: {my_list[1][-1]}")