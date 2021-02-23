# This will be an advanced password generator that will generate a password with a given length
# You will also decide if you want uppercase letters, lowercase letters, numbers or special characters
import random
# pyperclip will be the copy to clipboard tool

while True:
    print(
        "Welcome to Mack's Password Generator! Please answer a few questions and your password will be generated!"
    )
    continue

    print("How long do you want your password?")

    lengthResponse = input('')

    while True:
        if lengthResponse = int():
            lengthResponseInput == int(lengthResponse)
            continue
        else:
            break
            print("Please only use a whole number")
            

    print("Do you want uppercase letters? Y/N")

    upperResponse = input('')
    if upperResponse == 'Y' or upperResponse == 'y':
        upperResponseInput == True
        continue
    elif upperResponse == 'N' or upperResponse == 'n':
        upperResponseInput == False
        continue
    else:
        print("Please use only Y or N, case does not matter.")

    print("Do you want lowercase letters? Y/N")

    lowerResponse = input('')

    print("Do you want numbers/integers?")

    integerResponse = input('')

    print("Do you want special characters?")

    specCharResponse = input('')

