#Control structures and loops
'''Ex. 2 : Create a Python program that checks if a given number is prime or not. The user 
should input a number, and the program should print whether it is prime or not.'''

#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# For example, 2, 3, 5, 7, 11, 13, etc. are prime numbers. 
# A prime number cannot be written as a product of two smaller natural numbers

def prime():
    x = int(input("Enter a number: "))
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                print("Is not prime")
                break
        else:
            print("Is prime")
    else:
        print("Is not prime")


prime()

