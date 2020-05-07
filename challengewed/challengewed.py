#!usr/bine/env python3

num1= int(input("What is your first number? "))
num2= int(input("What is your second number? "))        
math = str(input("What action do you want to take? Add, Subtract, Multiply, Divide? "))
math = math.lower()        
def add (x,  y):
    sum= x+y
    return sum
def subtract (x,  y):
    sum= x-y
    return sum
def multiply (x,  y):
    sum= x*y
    return sum
def divide (x,  y):
    sum= x/y
    return sum

if math == "add":
    print(add(num1, num2)) 
elif math == "subtract":
    print(subtract(num1, num2))
elif math == "multiply":
    print(multiply(num1, num2))
elif math == "divide":
    print(divide(num1, num2))

        
