# This program will take in two variables - a string (type of currency) and an integer (value)
# Converts the value (integer) into a new integer (new value)
# I am turning money from one currency to another in this program

# Neat stuff about variables
# test_1, test_2, test_3 = 1, "two", False
# print('Test 1', test_1)
# print('Test 2', test_2)
# print('Test 3', test_3)

# This gets the value of currency

currency_value = input("Please give me the value in whole units of currency: ")
currency_value = int(currency_value)
currency_type = input("Please tell me the type of currency you are converting: ")
print(f"You currently have {currency_value} {currency_type}")
