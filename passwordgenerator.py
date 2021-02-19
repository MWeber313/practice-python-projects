import random

# This password generator will take 4 pairs of 4 different types of characters:
# lowercase, uppercase, integer, special character

# need to make a shuffle function:

def shuffle(string):
    tempString = list(string)
    random.shuffle(tempString)
    return ''.join(tempString)

# Upper Case 1
uppercaseLetter1=chr(random.randint(65,90))
print(uppercaseLetter1)

# Upper Case 2
uppercaseLetter2=chr(random.randint(65, 90))
print(uppercaseLetter2)

# Lower Case 1
lowercaseLetter1=chr(random.randint(97, 122))
print(lowercaseLetter1)

# Lower Case 2
lowercaseLetter2=chr(random.randint(97, 122))
print(lowercaseLetter2)

# Digit 1
digit1=str(int(random.randint(0, 999)))
print(digit1)

# Digit 2
digit2=str(int(random.randint(0, 999)))
print(digit2)

# Special Character 1
specialCharacter1=chr(random.randint(33, 96))
print(specialCharacter1)

# Special Character 2
specialCharacter2=chr(random.randint(33, 96))
print(specialCharacter2)

password=uppercaseLetter1+uppercaseLetter2+lowercaseLetter1+lowercaseLetter2+digit1+digit2+specialCharacter1+specialCharacter2
password=shuffle(password)
print(password)