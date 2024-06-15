> # AlgebraCalculator
>
> ### By Moli
>
> ![Static Badge](https://img.shields.io/badge/pypi-v1.0.5-blue) ![Static Badge](https://img.shields.io/badge/python-3-blue) ![Static Badge](https://img.shields.io/badge/licence-MIT-yellow)
---
## Install

```shell
# Windows
py -3 -m pip install algebraCalc
```
---
## Update
> ### Improved solveSystem function's algorithm
---
## Data Format
### Matrix
```Python
a = [[a11, a12, a13],
     [a21, a22, a23],
     [a31, a32, a33]] #where the value of the element is either int or float
#You can adjust the number of column and row, just make sure the length of the list is same each other
```
### Vector
```Python
a = [[a11, a12, a13]] #where the value of the element is either int or float
#a11 represent the value of i, a12 represent the value of j, a13 represent the value of k
```
---
## Frequently used function
### Matrix multiplication
```python
import algebraCalc
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[1],
     [2],
     [3]]
print(algebraCalc.multiplication(a, b))
# Output: [[14], [32], [50]]
```

### Dot product
```python
import algebraCalc
a = [[1, 2, 2]]
b = [[4, 5, 6]]
print(algebraCalc.dot(a, b))
# Output: 26
```
---
## Function List
```python
add(a, b) #return a matrix when matrix a and matrix b is added
det(a) #return the determinant of matrix a
inverse(a) #return the inverse of matrix a
adjoint(a) #return the adjoint matrix by matrix a
multiplication(a, b) #return a matrix when matrix a is multiplied by matrix b
transpose(a, b) #return a transpose matrix of a
dot(a, b) #return the dot product of vector a and vector b
cross(a, b) #return the cross product of vector a and vector b
angle(a, b) #return the angle between vector a and vector b
projection(a, b) #return the projection vector when vector a is projected onto vector b
scale(a, k) #return a matrix when a is multiplied by scalar k
printMatrix(a) #print matrix a
printVector(a) #print vector a
randomMatrix(row, col, min, max) #return a matrix with dimension row * col and random value at min to max
randomVector(min, max) #return a vector with random value at min to max
solveSystem(a, b) #return the solution of the system with matrix a as the coefficient matrix and b be the constant term matrix
```