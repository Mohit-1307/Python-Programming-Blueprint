# Check if the program is being run in an interactive shell
# try: 
#     x = int(input("What's x? "))
#     print(f"x is {x}")

# Handle the ValueError if the input is not an integer
# except ValueError: 
#     print("x is not an integer.")

# ---------------------------------------------------------------------------------------->

# try:
#     x = int(input("What's x? "))

# except ValueError:
#     print("x is not an integer.")

# else: 
#     print(f"x is {x}")

# ---------------------------------------------------------------------------------------->

# Loop until a valid integer is entered
# while True: 

#     # Check if the program is being run in an interactive shell
#     try:
#         x = int(input("What's x? "))

#     # Handle the ValueError if the input is not an integer
#     except ValueError:
#         print("x is not an integer.")

#     else:
#         break

# print(f"x is {x}")

# ---------------------------------------------------------------------------------------->

# while True:
    
#     try:
#         x = int(input("What's x? "))
#         break

#     except ValueError:
#         print("x is not an integer.")

# print(f"x is {x}")

# ---------------------------------------------------------------------------------------->

# def main(): 
    
#     x = get_integer()
    
#     print(f"x is {x}")

# def get_integer():
    
#     while True:
        
#         try:
#             x = int(input("What's x? "))

#         except ValueError:
#             print("x is not an integer.")
        
#         else:
#             break
    
#     return x

# main()

# ---------------------------------------------------------------------------------------->

# def main():

#     x = get_integer()

#     print(f"x is {x}")

# def get_integer():

#     while True:
        
#         try:
#             x = int(input("What's x? "))

#         except ValueError:
#             print("x is not an integer.")

#         else:
#             return x

# main()

# ---------------------------------------------------------------------------------------->

# def main():
    
#     x = get_integer("What's x? ")
    
#     print(f"x is {x}")

# def get_integer(prompt):
    
#     while True:
        
#         try:
#             return int(input(prompt))
        
#         except ValueError:
#             pass

# main()