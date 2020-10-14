if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) #use map to convert all the strings in a list to integers
    #convert the list into a tuple
    t = tuple(list(integer_list))
    output =  hash(t)
    print (output)