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

def insertMatrix(a: list) -> list:
    b = []
    for i in range(len(a[0])):
        b.append(a[0][i])
    return b

def solveSystem(a: list, b: list) -> list:
    argMatrix = []
    for i in range(len(a)):
        argMatrix.append([])
        for j in range(len(a)):
            argMatrix[i].append(a[i][j])
        argMatrix[i].append(b[i][0])
    for i in range(len(a)):
        if(argMatrix[i][i] != 0):
            argMatrix[i] = insertMatrix(scale([argMatrix[i]], 1 / argMatrix[i][i]))
        elif(i != len(a) - 1):
            temp = argMatrix[i + 1]
            argMatrix[i + 1] = argMatrix[i]
            argMatrix = temp
            argMatrix[i] = insertMatrix(scale([argMatrix[i]], 1 / argMatrix[i][i]))
        for j in range(i + 1, len(a)):
            if(argMatrix[i][i] != 0):
                argMatrix[j] = insertMatrix(add([argMatrix[j]], scale([argMatrix[i]], -argMatrix[j][i] / argMatrix[i][i])))
    if(argMatrix[len(argMatrix) - 1][len(argMatrix)] != 0 and argMatrix[len(argMatrix) - 1][len(argMatrix) - 1] == 0):
        raise ValueError("The system has no solution.")
    if(argMatrix[len(argMatrix) - 1][len(argMatrix)] == 0 and argMatrix[len(argMatrix) - 1][len(argMatrix) - 1] == 0):
        raise ValueError("The system has infinitely many solution.")
    sol = [[argMatrix[len(argMatrix) - 1][len(argMatrix)]]]
    for i in range(len(argMatrix) - 1):
        ans = argMatrix[len(argMatrix) - 2 - i][len(argMatrix)]
        for j in range(len(argMatrix)):
            ans = ans - argMatrix[len(argMatrix) - 2 - i][len(argMatrix) - 1 - j] * sol[0][len(sol[0]) - 1 - j]
            if(j >= i):
                break
        if(argMatrix[len(argMatrix) - 2 - i][len(argMatrix) - 2 - i] != 0):
            sol[0].insert(0, ans / argMatrix[len(argMatrix) - 2 - i][len(argMatrix) - 2 - i])
        elif():
            sol[0].insert(0, 0)
    return sol


        