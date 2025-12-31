# This print statement will throw an error because of the quotation marks.
# print("Hello, "friend"")


# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This print statement will print the string "Hello, 'friend'"" because the string is enclosed in double quotes.
# print("Hello, 'friend'")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This print statement will print the string "Hello, 'friend'"" because the string is enclosed in single quotes.
# print('Hello, "friend"')

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This print statement will print the string "Hello, 'friend'"" because we are using escape characters to avoid confusion with the quotation marks.
# print("Hello, \"friend\"")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# name = input("What's your name? ")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This is the one method to print the name.
# print("Hello, " + name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This is the other method to print the name there is no need to give extra space after Hello, because it have already added a space in the print statement.
# print("Hello,", name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will print the "Hello, and David in next line" because print have a newline by default.
# print("Hello,")
# print(name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will print the "Hello, David" without adding a new line because we have used the end = "" parameter.
# print("Hello, ", end = "")
# print(name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will print the "Hello, David" because print have a space by default.
# print("Hello,", name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will print the "Hello,David" because we have used the sep = "" parameter to remove the space.
# print("Hello,", name, sep = "")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will print the "Hello, {name}" because we have used the curly braces to print the name.
# print("Hello, {name}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will print the "Hello, David" because we have used the f-string to print the name.
# print(f"Hello, {name}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will remove the leading and trailing spaces from the name.
# name = name.strip()
# print(f"Hello, {name}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will capitalize the first letter of the name.
# name = name.capitalize()
# print(f"Hello, {name}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will capitalize the first letter of each word in the name.
# name = name.title()
# print(f"Hello, {name}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will remove the leading and trailing spaces from the name and then capitalize the first letter of each word in the name.
# name = name.strip().title()
# print(f"Hello, {name}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# This will split the name into two parts and store them in the variables first and last.
# first, last = name.split(" ")
# print(f"Hello, {last}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# FUNCTIONS
# This is a simple function that prints the "Hello, World" message and takes an optional parameter to greet someone else.
# def hello(to = "World"):
#     print("Hello,", to)

# Call the function without any argument to print the default greeting("Hello, World")
# hello() 
# name = input("What's your name? ")
# Call the function with an argument to print a custom greeting
# hello(name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------>

# We will define a main function that calls the hello function and takes user input.
# def main():
    
#     hello()
#     name = input("What's your name? ")
#     hello(name)

# This function prints the "Hello, World" message and takes an optional parameter to greet someone else.
# def hello(to = "World"):
#     print("Hello,", to)

# Call the main function to execute the code
# main()