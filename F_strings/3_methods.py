# String methods
# Capitialize will capitilize the first character
name = "iron man"
name.capitalize()

# Title will capitilize the first character of each word
name.title()

# Upper with capitilize all characters
name.upper()

# Lower will lower case all characters
name.lower()

# Find will find the beginning index
name.find("man")

# Count will count how many of the same characters
name.count("n")

# Index will find the index. Notice it only counts the first character, if there are multiple
name.index("n")

# Split will seperate select characters from string
name.split("ir")

# Replace will replace the string with something new (old string, new string)
name.replace("iron","super")

# Isupper will give you a true or false of truely upper case
name.isupper()

# Islower will give you a true or false for truely lower case
name.islower()

# Isnumeric will give you a true or false for truely numbers
name.isnumeric()

# Isalpha will give you a true of false for truely alphabets
name.isalpha()
# You will get a false for this because of the whitespace