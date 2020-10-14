import numpy

P = list(map(float,input().split()))
x = int(input())
value = numpy.polyval(P,x)
print (value)