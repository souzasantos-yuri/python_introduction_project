# Create a program that receives 4 heights, append them in a list and then show them

heights = []

for i in range(1,5):
    heights.append(int(input(f"Give me a total of 4 heights, this one being the #{i}: ")))

print(sum(heights))