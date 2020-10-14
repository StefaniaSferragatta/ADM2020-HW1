import numpy

N,M = map(int,input().split())
array = []
for _ in range(N):
    my_array = list(map(int,input().split()))
    array.append(my_array)
my_arr = numpy.array(array)
sum0 = numpy.sum(my_arr, axis=0)
prod = numpy.prod(sum0)
print(prod)