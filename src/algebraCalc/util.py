from .matrix import *
from .vector import *
import random

def scale(a: list, k: float) -> list:
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] =  k * a[i][j]
    return a

def printMatrix(a: list) -> None:
    for i in range(len(a)):
        if(i != 0):
            print()
        for j in a[i]:
            print(j, end=" ")
    print()

def printVector(a: list) -> None:
    print(str(a[0][0]) + "i + " + str(a[0][1]) + "j + " + str(a[0][2]) + "k")
    
def randomMatrix(row:int, col: int, min: int, max: int) -> list:
    newMatrix = []
    for i in range(row):
        newMatrix.append([])
        for j in range(col):
            newMatrix[i].append(random.randint(min, max))
    return newMatrix

def randomVector(min: int, max: int) -> list:
    return randomMatrix(1, 3, min, max)

def solveSystem(a: list, b: list) -> list:
    if (det(a) == 0):
        return None
    return multiplication(inverse(a), b)
