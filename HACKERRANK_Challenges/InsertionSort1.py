#Implementation of the 'inverse' Insertion sort (sorting from right to left)

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    index = n-1 #save the index of the last element of the array
    val = arr[index] #save the value of the index
    while(index>0 and val<arr[index-1]):
    #Moving the elements that are greater than value, to one position behind of their          current position
        arr[index] = arr[index-1]
        print(*arr) #Print the array as a row of space-separated integers at every modification (shift or insertion)
        index-=1 #decrease the index
    arr[index] = val #associate now the element with that new index at the
    print(*arr) #Print the final array as a row of space-separated integers

if __name__ == '__main__':
    n = int(input())
    if n>=1 and n <=1000:
        arr = list(map(int, input().rstrip().split()))
    #if arr[i]>=-1000 and arr[i]<= 1000:
    insertionSort1(n, arr)
