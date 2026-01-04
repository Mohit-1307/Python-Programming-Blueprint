# Import the requests module to make HTTP requests
# import requests 
# Import the sys module to get command line arguments
# import sys

# Check if the command line argument is provided
# if len(sys.argv) != 2:
#     sys.exit()

# Get the user's input as a command line argument
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# Print the JSON response in a readable format
# print(response.json()) 

# -------------------------------------------------------------------------------------------------------->

# Import json module to work with JSON data
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# This will make the JSON output more readable
# print(json.dumps(response.json(), indent = 2)) 

# -------------------------------------------------------------------------------------------------------->

# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# Get the song name from the command line argument
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) 
# Convert the JSON response to a Python dictionary
# object = response.json()

# Print the name of the first song found
# for result in object["results"]:
#     print(result["trackName"])