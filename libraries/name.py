# Import the sys module to access command line arguments
import sys 

# print("Hello, My name is", sys.argv[1])

# ------------------------------------------------------------------------------------>

# try:
#     print("Hello, My name is", sys.argv[1])

# except IndexError:
#     print("Too few arguments")

# ------------------------------------------------------------------------------------>

# if len(sys.argv) < 2:
#     print("Too few arguments")

# elif len(sys.argv) > 2:
#     print("Too many arguments")

# else:
#     print("Hello, My name is", sys.argv[1])

# ------------------------------------------------------------------------------------>

# We can pass multiple arguments in the command line like this if we set sys.argv[1]:
# python hello.py "Mohit Singh"

# ------------------------------------------------------------------------------------>

# Check the errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# Print name tags
# print("Hello, My name is", sys.argv[1])

# ------------------------------------------------------------------------------------>

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:]:
#     print("Hello, My name is", arg)