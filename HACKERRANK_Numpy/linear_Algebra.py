import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
det = numpy.linalg.det(A)
print(round(det, 2))