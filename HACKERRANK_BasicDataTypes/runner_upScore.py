if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n <= 10:
        arr = list(map(int, input().split()))
        print( max([i for i in arr if i < max(arr)])) #using list comprehensios