#Functions and data type
#Ex 2: Create a Python function called reverse_string that takes a string as input and returns the reversed string.

def reverse_string(x):
    y = reversed(x)
    for i in y:
        print(i, end="")

str_2 = 'ABC'

reverse_string(str_2)


