# Task 1: Calculate Factorial Using a Function

inpt = int(input("Enter the number here: "))
result = 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(inpt)
print("The Factorial of ", inpt,"is: " ,result)


# Task 2: Using the Math Module for Calculations
a = int(input("Enter a number here: "))

from math import sqrt, log, sin

print("The Square root of ", a ,"is: ", sqrt(a))
print("The Natural Logarithm of ", a ,"is: ", log(a))
print("The sine of ", a ,"is: ", sin(a))
