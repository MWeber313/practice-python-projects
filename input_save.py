# This project will take in an input
# This project will write to a file and save the note based on input
# EWventually you will be able to read the program (a la 'less' from Linux)

# A simple input

# in python 2 - you need to declare the type of input you are using, so if a string,
# please use quotes!

# print('Please type something here:')
# x = input("")
# print(type(x))
# response = "Hello, you said this: {}".format(x)
# print(response)

# x = raw_input('Please insert data here')
# print(x)
# print(type(x))

# please go here for more information between raw/reg raw_input
#https://www.python-course.eu/input.php

welcome = "Hello, welcome to the input_save program!"

print(welcome)

instruction = "Please choose an input type"
print('raw')
print('standard')

answer1 = raw_input()

if answer1 == 'raw':
    print('Thank you for choosing Raw Input')
    

else:
    print('Thank you for choosing Standard Input!')
    print('Please declare your type with quotes for strings\ capitals for Booleans, and plain \ numbers for integers')
print()
