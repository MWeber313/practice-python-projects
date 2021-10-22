# The purpose of this program is to give the user a password
# This password will be generated based on user inputs
# This generator will pull from the user's inputs
# Variables in the password:
## Upper/Lowercase letters
## Numbers
## Symbols

# # This accepts the length of the password
passLength = input('Please declare the length of your password: ')

# # input automatically converts to string, this makes integer
passLength = int(passLength)
# print(type(passLength))
# 10/21 - This works
# print(passLength)

# The following queries and variables confirm password generation

# upperQuery = input('Uppercase letters? (Y/N) ')
# upperVar = False
# if upperQuery == 'Y' or upperQuery == 'y':
#     upperVar = True


# lowerQuery = input('Lowercase letters? (Y/N) ')
# lowerVar = False
# if lowerQuery == 'Y' or lowerQuery == 'y':
#     lowerVar = True

# numberQuery = input('Numbers? (Y/N) ')
# numberVar = False
# if numberQuery == 'Y' or numberQuery == 'y':
#     numberVar = True

symbolQuery = input('Special characters? (Y/N) ')
symbolVar = False
if symbolQuery == 'Y' or symbolQuery == 'y':
    symbolVar = True

print(
    passLength
)
