# Remove leading and trailing whitespace from the email input
# email = input("What's your email? ").strip() 

# Split the email address into username and domain parts
# username, domain = email.split("@")

# # Validate the email format
# if username and domain.endswith(".edu"):
#     print("Valid email")

# else:
#     print("Invalid email")

# ------------------------------------------------------------------------>

# Validate the email format using regular expressions
# import re

# email = input("What's your email? ").strip()

# Use the regular expression to match the email format
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid email")

# else:
#     print("Invalid email")

# ------------------------------------------------------------------------>

# Validate the email format using regular expressions
# import re

# email = input("What's your email? ").strip()

# Use the regular expression to match the email format
# we can use "\w" instead of "[a-zA-Z0-9_]+" to match any alphanumeric characters or underscores and (\w|space) for space
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net)$", email, re.IGNORECASE): 
#     print("Valid email")

# else:
#     print("Invalid email")