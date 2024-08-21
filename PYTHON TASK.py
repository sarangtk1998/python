Number=int(input("Please enter a number"))
if Number==0:
    print('The entered number', Number, ' is Zero')
elif Number%2==0:
    print('The entered number',Number, 'is even')
else:
    print('The entered number', Number, 'is odd')

def leap_year(year):
    if year%4==0:
        return 'entered year',year, 'is a leap year'

    elif year%100==0:
        return 'entered year', year, 'is a leap year'
    elif year%400==0:
        return 'entered year', year, 'is a leap year'
    else:
        return 'entered year', year, 'is not a leap year'
x=leap_year(2023)
print(x)

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))
if number1>number2 and number1>number3:
    print('number1:',number1,'is largest among three numbers')
elif number2>number1 and number2>number3:
    print('number2:',number2,'is largest among three numbers')
else:
    print('number3:',number3,'is largest among three numbers')

age = int(input("Please enter your age: "))
sex = input("Please enter your sex (male/female): ")
days = int(input("Please enter the number of working days: "))
if 18<=age<30:
    if sex=='male':
        print('dailywage=700')
        Total_wage=days*700
        print('Total_wage is',Total_wage)
    elif sex=='female':
        print('dailywage=750')
        Total_wage = days * 750
        print('Total_wage is', Total_wage)
    else:
        print("Invalid input")
elif 30<=age<=40:
    if sex == 'male':
        print('dailywage==800')
        Total_wage = days * 800
        print('Total_wage is', Total_wage)
    elif sex == 'female':
        print('dailywage=850')
        Total_wage = days * 850
        print('Total_wage is', Total_wage)
    else:
        print("Invalid input")
else:
    print("Invalid input")




quantity =int(input("Please enter the quantity of items you want to purchase: "))
discount_condition=1000
discount_rate=0.1#10%
unit_cost=100
Total_cost=quantity*unit_cost
if Total_cost>discount_condition:
    discount=Total_cost*discount_rate
    Total_cost-=discount

print(Total_cost)

x=float(input('Enter one side of a traiangle:'))
y=float(input('Enter second side of a traiangle:'))
z=float(input('Enter third side of a traiangle:'))
if x==y==z:
    print("This is an equilateral triangle in which three sides are equal")
elif x!=y!=z:
    print("This is a scalene triangle that has three unequal sides")
elif x==y or y==z or x==z:
    print("This is an isosceles triangle")
else:
    print("Invalid input")

First_number=float(input("Enter your first number:"))
Second_numnber=float(input("Enter your second number:"))
Operator=input("Enter the operator")
if Operator=="+":
    result=First_number+Second_numnber
    print("You have selected addition operator and the result is,",result)

elif Operator=="-":
    result = First_number - Second_numnber
    print("You have selected substraction operator and the result is,", result)
elif Operator=="*":
    result = First_number * Second_numnber
    print("You have selected multiplication operator and the result is,", result)
elif Operator=="/":
    result = First_number / Second_numnber
    print("You have selected division operator and the result is,", result)
elif Operator=="%":
    result = First_number % Second_numnber
    print("You have selected modulus operator and the result is,", result)
elif Operator=="**":
    result = First_number ** Second_numnber
    print("You have selected power/exponential operator and the result is,", result)
elif Operator=="//":
    result = First_number // Second_numnber
    print("You have selected floor division operator and the result is,", result)
else:
    print("You have selected wrong operator")

Mark=float(input("Please enter your obtained mark to determine the grade:"))
if Mark<25:
    print("Your grade is F")
elif 25<Mark<45:
    print("Your grade is E")
elif 45<Mark<50:
    print("your grade is D")
elif 50<Mark<60:
    print("Your grade is C")
elif 60<Mark<80:
    print("Your grade is B")
else:
    print("You are awarded A Grade")

city=input("Enter the city that you want to know the monument of it:")
if city=='Delhi':
    print("The monument of Delhi is Redfort")
elif city=='Agra':
    print("The monument of Agra is Taj Mahal")
elif city=='Jaipur':
    print("The monument of Jaipur is Jai Mahal")
else:
    print("Monument not found")

length = float(input("Please enter the length of the rectangle: "))
breadth = float(input("Please enter the breadth of the rectangle: "))


if length == breadth:
    print("The shape is a square.")
else:
    print("The shape is a rectangle.")