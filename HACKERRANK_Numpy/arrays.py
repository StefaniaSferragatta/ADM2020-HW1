import numpy

def arrays(arr):
    my_array = numpy.array(arr[::-1], float)
    return my_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)