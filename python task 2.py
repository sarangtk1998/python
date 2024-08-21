import keyword
kw=keyword.kwlist
user_input = input("Enter a string to check if it is a valid identifier: ")
valid = True
if len(user_input) == 0:
    valid = False
else:
    if not user_input[0].isalpha() or user_input[0] == '_':
        valid = False
        for i in user_input[1:]:
            if not (i.isalnum() or i == '_'):
                valid = False
                break

if user_input in kw:
    valid = False

if valid:
    print(user_input,"is a valid identifier.")
else:
    print(user_input,"is not a valid identifier.")

def is_valid_identifier(input_string):
    if not input_string:
        return False
    if not (input_string[0].isalpha() or input_string[0] == '_'):
        return False
    for i in input_string[1:]:
        if not (i.isalnum() or i == '_'):
            return False

    return True
def find_valid_identifiers(input_string):
    identifiers = input_string.split()
    valid_identifiers = []

    for identifier in identifiers:
        if is_valid_identifier(identifier):
            valid_identifiers.append(identifier)

    return valid_identifiers

input_string = "_validIdentifier1 2InvalidIdentifier valid_123 __init__ invalid-identifier _valid1 valid _ 1invalid valid123"

valid_identifiers = find_valid_identifiers(input_string)
print("Valid identifiers:", valid_identifiers)


number1=int(input("enter your first number:"))
number2=int(input("enter your second number:"))
number3=int(input("enter your third number:"))
sum_of_3_numbers=number1+number2+number3
print(sum_of_3_numbers)

import string
import itertools
n = int(input("Enter the length of the identifiers to generate: "))
first_chars = string.ascii_letters + '_'
subsequent_chars = string.ascii_letters + string.digits + '_'
identifiers = []
if n == 1:
    for i in first_chars:
        identifiers.append(i)
else:
    combinations = itertools.product(subsequent_chars, repeat=n - 1)
    for combination in combinations:
        for first_char in first_chars:
            identifier = first_char + ''.join(combination)
            identifiers.append(identifier)
print('All possible valid identifiers of length', n,':')
for identifier in identifiers:
    print(identifier)

list_of_numbers = list(input("Please enter a list of numbers:"))
max_num=max(list_of_numbers)
min_num=min(list_of_numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

num1=int(input("Please enter number1:"))
num2=int(input('Please enter your second number:'))
#Addition
result=num1+num2
print('Addition result:',result)
#substraction
result=num1-num2
print("subtraction result:",result)
#Multiplication
result=num1*num2
print("Multiplication result:",result)
#Division
result=num1/num2
print('Division result:',result)
#Modulus
result=num1%num2
print('Modulus result:',result)
#Exponential/power
result=num1**num2
print('Exponential result:',result)
#Floor Division
result=num1//num2
print('Floor division result:',result)

First_number=int(input('Enter the first number:'))
Second_number=int(input('Enter the second number:'))
#Equal operator
result=First_number==Second_number
print('Equal result:',result)
#Less than operator
result=First_number<Second_number
print('Less than result:',result)
#Greater than operator
result=First_number>Second_number
print("Greater than result:",result)
#Less than or equal to operator
result=First_number<=Second_number
print("Less than or equal to:",result)
#Greaterthan or equal to operator
result=First_number>=Second_number
print("Greater than or equal to:",result)
#Not equal to operator
result=First_number!=Second_number
print("Not equal to:",result)

age=int(input("Please Enter your age?"))
if age>=18 and age<=120:
    print(" you are eligible to vote")
else:
    print('your age is',age,'which is below 18,so you are not eligible to vote')

#Multiplication table
num=int(input("Enter the number to print multiplication table:"))
for i in range(1,11):
    result=i*num
    print( i, "*",num,"=",result)

#Factorial of a number
Number=int(input("Enter the number to find the factorial:"))
if Number==0:
    print("Factorial of 0 is 1")
elif Number<0:
    print("Negative numbers have no factorial")
else:
    factorial = 1
    for i in range(Number,0,-1):

        factorial=factorial*i
    print("factorial of",Number,"is:",factorial)