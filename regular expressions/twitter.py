# url = input("URL: ").strip()

# Remove the "https://" and ".com" from the URL
# username = url.replace("https://twitter.com", "")

# print(f"Username: {username}")

# ------------------------------------------------------------------------>

# Importing the re module for regular expressions
# import re

# url = input("URL: ").strip()

# Remove the "https://" and ".com" from the URL using regular expressions
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com", "", url)

# We are using the re.search() function to find the first match of the pattern in the URL
# matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)

# Check if a match was found
# if matches:
#     print(f"Username: {matches.group(1)}")