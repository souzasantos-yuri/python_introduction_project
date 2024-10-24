# Create a program that receives 4 grades from a student. Return the average of these grades, the lowest grade, and the highest grade.

grades = []

for i in range(0, 4):
    grades.append(int(input(f"Give me 4 grades, this one is the #{i + 1}: ")))

grades.sort()

avg_grades = sum(grades) / len(grades)
lowest_grade = grades[0]
highest_grade = grades[-1]

print(f"Average: {avg_grades}")
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")