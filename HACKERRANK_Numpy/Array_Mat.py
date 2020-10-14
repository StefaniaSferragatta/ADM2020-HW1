
import numpy

N,M = map(int,input().split())
for _ in range(N):
    A = numpy.array(input().split(), float)
    B = numpy.array(input().split(), float)

#ADD
print (numpy.add(A, B))
#SUBTRACT
print (numpy.subtract(A, B))
#MULTIPLY
print (numpy.multiply(A, B))
#INTEGER DIVISION
print (numpy.divide(A, B))
#MOD
print (numpy.mod(A, B))
#POWER
print (numpy.power(A, B))