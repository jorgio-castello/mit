# MIT Introduction to Programmming, Course 6.0001
# Jorge Castello, jorgio.castello@gmail.com
# https://github.com/jorgio-castello

import numpy as np

# If a float could possibly be presented as an int without losing meaning
def generateIntOrFloat(num: int or float) -> int or float:
    if num % 1 == 0:
        return int(num)
    return num

# Converts user input string to a number
def convertUserInput(numStr: str) -> int or float:
    if numStr.find('.') > 0:
        return float(numStr)
    return int(numStr)

# Calculates the power of x ** y
def calculatePower(x: int or float, y: int or float) -> int or float:
    return generateIntOrFloat(x ** y)

# Calculates the base-2 log of x
def calculateLog(x: int or float) -> int or float:
    return generateIntOrFloat(np.log2(x))

# User Control
def userInput():
    #Variables to obtain user input
    x:str = input('\nEnter number x: ')
    y:str = input('Enter number y: ')
    
    # Convert user input to int or float
    x:int or float = convertUserInput(x)
    y:int or float =  convertUserInput(y)

    # Calculations of x ** y, and log(x)
    power = calculatePower(x, y)
    log = calculateLog(x)

    # Print
    print('\nx ** y = ' + str(power))
    print('log(x) = ' + str(log))

# User Input: 1 - Enter numbers, 2 - Run Tests, 3 - End Program
program = input('\nWelcome to Powers and Logs! \n\nHere are your options:\n1. Choose your numbers\n2. End Program\n\nPlease Enter a Number: ')
program = convertUserInput(program)

# Control Flow: 
while program is 1:
    if program is 1:
        userInput()
    program = input('\nWould you like to continue?\n1. Choose your numbers\n2. End Program\n\nPlease Enter a Number: ')
    program = convertUserInput(program)

if (program == 2):
    print('Bye bye!')