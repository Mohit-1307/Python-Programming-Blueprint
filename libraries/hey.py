# Import the sys module to access command line arguments
import sys 
# Import the hello function from the Sayings module
from sayings import hello 

# Check if the user provided a name as a command line argument
if len(sys.argv) == 2:
    hello(sys.argv[1])