#Exercise 1: Write a Python program that takes two numbers as input from the user and prints their sum.

def suma(a,b):
    print (f'{a} + {b} = {a + b}')

a = float(input('enter a number: '))
b = float(input(f'enter a number to add to {a}: '))

suma(a,b)


