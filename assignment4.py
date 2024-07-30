#1. Python List Transformation

#Objective: The aim of this assignment is to practice list operations and transformations.

#Problem Statement: 
# You've been given a list of grades from an exam. You need to process and analyze these grades.

#Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print(grades)

#Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)

#Task 2: Calculate the average grade and print it.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average = sum(grades) / len(grades)
print(int(average))

# 2. Advanced List Methods and Identity Operators
# Problem Statement: 
# You have two lists of student names. 
# One list contains the names of students who have submitted their assignments, 
# and the other list contains the names of students who attended the last class.

#Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out if Alice submitted their assignment and attended class. 
# HINT: How might the in keyword be of use here? 
print("Alice" in submitted)
print("Alice" in attended)

# And how can you check to see if Alice is in both submitted and attended in one if statement?

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print ("True") if "Alice" in submitted and "Alice" in attended else ("False")

#3. Advanced Slicing Techniques

#Objective: The aim of this assignment is to use Python list slicing.
#Problem Statement: 
# You have a list of daily temperatures for one month, and you'd like to extract specific data from it.

#Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:

#83, 85, 86, 87, 88, 89, 90,

picked_temperatures = temperatures[7:14]
print(picked_temperatures)

# Task 2: 
# Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

above_100_temp = temperatures[24:]
print(above_100_temp)

# Note:
#Ensure that all code in your file is ready to run. 
# This means that if someone opens your file and clicks the run button at the top, 
# all code executes as intended. For example, if there are if statements or print statements, 
# they should function correctly and display output in the console as expected.

