import numpy
N =int(input())
A =numpy.array([input().split() for _ in range(N)],int)
B =numpy.array([input().split() for _ in range(N)],int)
matrix_mult = numpy.dot(A, B)
print (matrix_mult)