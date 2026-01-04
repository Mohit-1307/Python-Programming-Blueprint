# This module provides a simple interface to cowsay
import cowsay 
# Import the sys module to get command line arguments
import sys

# Print a cow saying "hello, world!" if no argument is provided
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])


if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])