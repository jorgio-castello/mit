# MIT Introduction to Programmming, Course 6.0001
# Jorge Castello, jorgio.castello@gmail.com
# https://github.com/jorgio-castello

import numpy as np

def generateIntOrFloat(num: int or float) -> int or float:
    if num % 1 == 0:
        return int(num)
    return num

def convertUserInput(numStr: str) -> int or float:
    if numStr.find('.') > 0:
        return float(numStr)
    return int(numStr)

#Variables to obtain user input
x:str = input('Enter number x: ')
y:str = input('Enter number y: ')

# Convert user input to int or float
x:int or float = convertUserInput(x)
y:int or float =  convertUserInput(y)

# Calculations of x ** y, and log(x)
power = x ** y
log = np.log2(x)
log = generateIntOrFloat(log) # Determine whether log is float or int

# Print
print('x ** y = ' + str(power))
print('log(x) = ' + str(log))

