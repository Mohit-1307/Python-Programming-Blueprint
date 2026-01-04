# name = input("What's your name? ").strip()

# Check if the name contains a comma and split it into first and last names
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"Hello, {name}")

# ------------------------------------------------------------------------>

# Import the re module for regular expressions
# import re

# name = input("What's your name? ").strip()

# Check if the name contains a comma and split it into first and last names using regular expressions
# if matches := re.search(r"^(.+), *(.+)$", name):
    # # last, first = matches.groups()
    # # last = matches.group(1)
    # # first = matches.group(2)
    # # name = f"{first} {last}"
    # name = matches.group(2) + " " + matches.group(1)

# print(f"Hello, {name}")