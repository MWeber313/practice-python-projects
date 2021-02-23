# This will be an advanced password generator that will generate a password with a given length
# You will also decide if you want uppercase letters, lowercase letters, numbers or special characters
import random
import math
# pyperclip will be the copy to clipboard tool

# While loop for the program
while True:
    print(
        "Welcome to Mack's Password Generator! Please answer a few questions and your password will be generated!"
    )
    

    print("How long do you want your password?")

    lengthResponse = input('')

    while True:
        if type(lengthResponse) is int:
            lengthResponseInput == int(lengthResponse)
            continue
        else:
            break
            print("Please only use a whole number")
            
    print("Do you want uppercase letters? Y/N")

    upperResponse = input('')

    while True:
        if isInstance(upperResponse, str):
            print(type(upperResponse))
            print("Response must be a string")
            break

        elif upperResponse == 'Y' or upperResponse == 'y':
            upperResponseInput = True
            continue
        elif upperResponse == 'N' or upperResponse == 'n':
            upperResponseInput = False
            continue
        else:
            print("Please use only Y or N, case does not matter.")

    print("Do you want lowercase letters? Y/N")

    lowerResponse = input('')

    while True:
        if lowerResponse != str:
            print("Response must be a string")
            break
        if lowerResponse == 'Y' or lowerResponse == 'y':
            lowerResponseInput = True
            continue
        elif lowerResponse == 'N' or lowerResponse == 'n':
            lowerResponseInput = False
            continue
        else:
            print("Please use only Y or N, case does not matter.")

    print("Do you want numbers/integers?")

    integerResponse = input('')

    while True:
        if integerResponse != str:
                print("Response must be a string")
                break
        if integerResponse == 'Y' or integerResponse == 'y':
            integerResponseInput = True
            continue
        elif integerResponse == 'N' or integerResponse == 'n':
            integerResponseInput = False
            continue
        else:
            print("Please use only Y or N, case does not matter.")

    print("Do you want special characters?")

    specCharResponse = input('')

    while True:
        if specCharResponse != str:
            print("Response must be a string")
            break
        if specCharResponse == 'Y' or specCharResponse == 'y':
            specCharResponseInput = True
            continue
        elif specCharResponse == 'N' or specCharResponse == 'n':
            specCharResponseInput = False
            continue
        else:
            print("Please use only Y or N, case does not matter.")

    break

while True:
    count = 0
    if upperResponseInput == True:
        count +=1
    else:
        continue
    
    if lowerResponseInput == True:
        count +=1
    else:
        continue

    if integerResponseInput == True:
        count +=1
    else:
        continue

    if specCharResponseInput == True:
        count +=1
    else:
        continue

    totalAvg = (totalAvg // count)

    print(totalAvg)