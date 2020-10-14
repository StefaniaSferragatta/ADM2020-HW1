import numpy

N,M = map(int,input().split())
array = []
for _ in range(N):
    my_array = list(map(int,input().split()))
    array.append(my_array)
my_arr = numpy.array(array)
output = numpy.min(my_arr, axis=1)
print(max(output))
