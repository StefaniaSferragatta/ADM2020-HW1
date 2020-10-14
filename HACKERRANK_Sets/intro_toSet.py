def average(array):
    # your code goes here
    array = set(array)
    s = sum(array)
    l = len(array)
    average = s/l
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)