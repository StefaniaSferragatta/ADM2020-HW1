K = int(input())
s = input().split()
if K > 1 and K < 1000:
    #Create two empty sets.
    s1 = set()  # all unique room number
    s2 = set()  # all unique room number occur more than once
    #For each array element, if it isn't in the set of the unique room number, add to it
    for i in s:
        if i in s1:
            s2.add(i)
        else: #otherwise,it's in add it to the second
            s1.add(i)
    s3 = s1.difference(s2) #the only number that didn't appear K times is our output
    output = list(s3) #convert the set into a string in order to print the element
    print(output[0])