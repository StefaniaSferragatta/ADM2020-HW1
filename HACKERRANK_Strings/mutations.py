def mutate_string(string, position, character):
    #convert the string in input in a list
    l = list (string)
    #then do the change in the list
    l[position] = character
    #after that, convert the list into the new string
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    if c.isalpha(): #check that che character is a string
        s_new = mutate_string(s, int(i), c)
    else:
        print ("Invalid input")
    print(s_new)