import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
numpy.set_printoptions(legacy='1.13')
print(A.mean(axis=1))
print(A.var(axis=0))
print(A.std())