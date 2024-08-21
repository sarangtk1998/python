#1 To identify the given string is an identifier or not

# a=input('Enter any string :')
# if a.isidentifier():
#     print('The given string is an identifier')
# else:
#     print('The given string is not an identifier')

#2 To find all the valid identifier in the given string
# a='if','else','ramu','3454','_raju','$#%&%'
# identifier=[]
# for i in a:
#     if i.isidentifier():
#         identifier.append(i)
# print(identifier)



#3 sum of 3 numbers

# a=int(input('Enter num1 :'))
# b=int(input('Enter num2 :'))
# c=int(input('Enter num3 :'))
#
# sum=a+b+c
# print(sum)

#4 To generate all possible valid identifier of given length
keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while",
    "with", "yield"
]

n = int(input("Enter the length of the identifier: "))

string= []

for i in keywords:
    if len(i) == n:
        string.append(i)
print(string)

#5 find max and min numbers from a list of numbers
#
# input = input("Enter the list of numbers : ")
#
# numbers = []
#
# for i in input:
#     numbers.append(int(i))
#
# max_number = max(numbers)
# min_number = min(numbers)
# print(max_number,min_number)


#6 Arithemethic operators function

# a=int(input('Enter num1 :'))
# b=int(input('Enter num2 :'))
#
# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# mod=a%b
#
# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)


#7 To comare the numbers
# num1=float(input('Enter num1:'))
# num2=float(input('Enter num2:'))
# if num1>num2:
#     print('print num1 is greater then num2')
# elif num1==num2:
#     print('num1 and num2 are equal')
# elif num1<num2:
#     print('num2 is greater than num1')
# else:
#     print('num1 is nut equal to num2')



#8 Voting
# age=int(input('Enter your age :'))
# if 18<=age<=120:
#     print('you are eligible for voting')
# else:
#     print('you are not eligible for voting')


#9 To print Multiplication Table
# num=int(input('Enter a number:'))
# print(f'The Multiplication Table of {num} is:')
# for i in range(1,11):
#     print(f'{num} X {i} = {num * i}')




# 10 To find the factorial of a number

# n = int(input('Enter a number :' ))
#
# if n < 0:
#     print('No factorial for negative numbers.')
# elif n == 0 or n == 1:
#     print("1")
# else:
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     print(result)

