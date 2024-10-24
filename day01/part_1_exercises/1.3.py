#Create a program that receives the radius of a circle in centimeters. Return to the user the area and perimeter of this circle in the following format:
#Area: x.xx
#Perimeter: y.yy"

radius = int(input("Tell me the radius of your circle: "))

perimeter = format(radius * 3.14 * 2, '.2f')
area = format((radius ** 2) * 3.14, '.2f')

print(f"The perimeter is approximately {perimeter} cm")
print(f"The area is approximately {area} cm")