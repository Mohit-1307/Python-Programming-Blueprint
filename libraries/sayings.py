# The main function contains two calls to the hello() and goodbye() functions.
def main(): 
    hello("world")
    goodbye("world")

# Prints a greeting message.
def hello(name): 
    print(f"Hello, {name}!")

# Prints a farewell message.
def goodbye(name): 
    print(f"Goodbye, {name}!")

# This line ensures that the main function is executed only when the script is run directly, not when it's imported as a module.
if __name__ == "__main__":
    main()