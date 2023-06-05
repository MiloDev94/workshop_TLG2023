'''Exercise 2: Create a Python program that converts a temperature from Fahrenheit to Celsius. 
The user should enter the temperature in Fahrenheit, and the program should print 
the equivalent temperature in Celsius'''

def fht_to_cel():
    f_t = float(input('Enter the tempeture in fahrenheit degrees: '))
    celsius = round((f_t - 32)*(5/9), 2)
    print(f'Tempeture in celsius degress is: {celsius}')
    

fht_to_cel()



