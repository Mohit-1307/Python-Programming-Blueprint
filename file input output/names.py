# name = input("What's your name? ")

# # Create a new file or overwrite the existing one.
# file = open("names.txt", "w")

# # Write the name to the file.
# file.write(name)

# # Close the file.
# file.close()

# -------------------------------------------------------------------------------------------------------------------------------->

# name = input("What's your name? ")

# Open the file in append mode. This will add the name to the existing file if it exists,
# or create a new file if it doesn't exist and append the name without overwriting the existing content but not in the next line.
# file = open("names.txt", "a")

# file.write(name)

# file.close()

# -------------------------------------------------------------------------------------------------------------------------------->

# name = input("What's your name? ")

# file = open("names.txt", "a")

# Write the name to the file with a newline character at the end. This will add a new line after each name written to the file.
# file.write(f"{name}\n")

# file.close()

# -------------------------------------------------------------------------------------------------------------------------------->

# name = input("What's your name? ")

# The 'with' statement automatically closes the file after the block of code is executed.
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# -------------------------------------------------------------------------------------------------------------------------------->

# Read the content of the file.
# with open("names.txt", "r") as file:
    # Read the content of the file as a list of lines.
    # lines = file.readlines()

# Print "Hello," followed by each name in the file.
# for line in lines:
    # print("Hello,", line)

# -------------------------------------------------------------------------------------------------------------------------------->

# Read the content of the file.
# with open("names.txt", "r") as file:
#     for line in file:
#         # rstrip() removes the trailing newline character from each line before printing it.
#         print("Hello,", line.rstrip())

# -------------------------------------------------------------------------------------------------------------------------------->

# Create an empty list to store the names.
# names = []

# Read the content of the file and add each name to the list.
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# Print "Hello," followed by each name in the sorted list.
# for name in sorted(names):
#     print(f"Hello, {name}")

# -------------------------------------------------------------------------------------------------------------------------------->

# Read the content of the file and print "Hello," followed by each name in sorted order
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello,", line.rstrip())

# -------------------------------------------------------------------------------------------------------------------------------->

# Read the content of the file and print "Hello," followed by each name in reverse sorted order
# with open("names.txt") as file:
#     for line in sorted(file, reverse = True):
#         print("Hello,", line.rstrip())