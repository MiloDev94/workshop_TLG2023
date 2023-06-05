#CONTROL STRUCTURE
#Ex_1: Write a Python program that prints the first 10 Fibonacci numbers using a loop

#First 10 fibonacci numbers: 0,1,1,2,3,5,8,13,21,34.  F0 = 0, F1 = 1, Fn = Fn-2  + Fn-1

fibonacci_numbers = [0,1]
n = 2

while n <10:
    fibonacci_numbers.append(fibonacci_numbers[n-2] + fibonacci_numbers[n-1])
    n += 1

print(fibonacci_numbers)

