# Open the students.csv file in read mode
# with open("students.csv") as file:
#     for line in file:
        # Remove the trailing newline character and split the line into a list of strings by comma
        # row = line.rstrip().split(",")
        # Print the formatted string using the first and second elements of the list
        # print(f"{row[0]} is in {row[1]}")

# ------------------------------------------------------------------------------------------------------------------>

# Open the students.csv file in read mode
# with open("students.csv") as file:
#     for line in file:
        # Remove the trailing newline character and split the line into a list of strings by comma
        # name, house = line.rstrip().split(",")
        # Print the formatted string using the first and second elements of the list
        # print(f"Name: {name} House: {house}")

# ------------------------------------------------------------------------------------------------------------------>

# Open the students.csv file in read mode
# with open("students.csv") as file:
    # Sort the lines in the file based on the first element (name) in ascending order
    # for line in sorted(file):
        # Remove the trailing newline character and split the line into a list of strings by comma
        # name, house = line.rstrip().split(",")
        # Print the formatted string using the first and second elements of the list
        # print(f"Name: {name} House: {house}")

# ------------------------------------------------------------------------------------------------------------------>

# Create an empty list to store the students name and house
# students = []

# Open the students.csv file in read mode
# with open("students.csv") as file:
    # Iterate through each line in the file
    # for line in file:
        # Remove the trailing newline character and split the line into a list of strings by comma
        # name, house = line.rstrip().split(",")
        # Append the formatted string using the first and second elements of the list to the students list
        # students.append(f"Name: {name} House: {house}")

# Sort the students list based on the first element(name) in ascending order and print each student
# for student in sorted(students):
#     print(student)

# ------------------------------------------------------------------------------------------------------------------>

# create an empty list to store the students dictionary
# students = []

# Open the students.csv file in read mode
# with open("students.csv") as file:
    # Iterate through each line in the file
    # for line in file:
        # Remove the trailing newline character and split the line into a list of strings by comma
        # name, house = line.rstrip().split(",")
        # Create a dictionary with the first element as the key and the second element as the value
        # student = {"name": name, "house": house}
        # Append the student dictionary to the students list
        # students.append(student)

# Define a function to get the name of the student from the dictionary
# def get_name(student):
#     return student["name"]

# Sort the students list based on the name in ascending order and print each student
# for student in sorted(students, key = get_name):
#     print(f"Name: {student['name']} House: {student['house']}")

# ------------------------------------------------------------------------------------------------------------------>

# create an empty list to store the students dictionary
# students = []

# Open the students.csv file in read mode
# with open("students.csv") as file:
    # Iterate through each line in the file
    # for line in file:
        # Remove the trailing newline character and split the line into a list of strings by comma
        # name, house = line.rstrip().split(",")
        # Create a dictionary with the first element as the key and the second element as the value
        # student = {"name": name, "house": house}
        # Append the student dictionary to the students list
        # students.append(student)

# Sort the students list based on the name in ascending order and print each student
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"Name: {student['name']} House: {student['house']}")

# ------------------------------------------------------------------------------------------------------------------>

# Import the csv module to read CSV files
# import csv

# create an empty list to store the students dictionary
# students = []

# Open the students.csv file in read mode
# with open("students.csv") as file:
#     # Use the csv.reader to read the file
#     reader = csv.reader(file)
#     # Iterate through each row in the CSV file
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# Sort the students list based on the name in ascending order and print each student
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"Name: {student['name']} Home: {student['home']}")

# ------------------------------------------------------------------------------------------------------------------>

# Import the csv module to read CSV files
# import csv

# create an empty list to store the students dictionary
# students = []

# Open the students.csv file in read mode
# with open("students.csv") as file:
#     # Use the csv.reader to read the file
#     reader = csv.DictReader(file)
#     # Iterate through each row in the CSV file
#     for row in reader:
#         students.append(row)

# Sort the students list based on the name in ascending order and print each student
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"Name: {student['name']} Home: {student['home']}")

# ------------------------------------------------------------------------------------------------------------------>

# import csv

# name = input("What's your name? ")
# home = input("Where is your home? ")

# Open the students.csv file in append mode (a)
# with open("students.csv", "a") as file:
#     # Use the csv.writer to write the new student to the file
#     writer = csv.writer(file)
#     # Write the new student to the file as a new row (w)
#     writer.writerow([name, home])

# ------------------------------------------------------------------------------------------------------------------>

# import csv

# name = input("What's your name? ")
# home = input("Where is your home? ")

# with open("students.csv", "a") as file:
#     # Use the csv.DictWriter to write the new student to the file
#     writer = csv.DictWriter(file, fieldnames = ["name", "home"])
#     # Write the new student to the file as a new row (w)
#     writer.writerow({"name": name, "home": home})