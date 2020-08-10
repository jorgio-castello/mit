# MIT Introduction to Programmming, Course 6.0001
# Jorge Castello, jorgio.castello@gmail.com
# https://github.com/jorgio-castello

import sys
import json
import numpy as np

# If a float could possibly be presented as an int without losing meaning
def generateIntOrFloat(num: int or float) -> int or float:
    if num % 1 == 0:
        return int(num)
    return num

# Calculates the power of x ** y
def calculatePower(x: int or float, y: int or float) -> int or float:
    return generateIntOrFloat(x ** y)

# Calculates the base-2 log of x
def calculateLog(x: int or float) -> int or float:
    return generateIntOrFloat(np.log2(x))

def generateTuple(x: int or float, y: int or float) -> [int or float]:
    result = {}
    result['power'] = calculatePower(x, y)
    result['log'] = calculateLog(x)
    return result

def init(data: json) -> [tuple]:
    result = {}
    inputData = json.loads(data)
    for inp in inputData:
        key = json.dumps(inp)
        result[key] = generateTuple(inp['x'], inp['y'])
    print(result)

init(sys.argv[1])