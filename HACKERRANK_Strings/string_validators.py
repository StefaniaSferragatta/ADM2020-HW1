if __name__ == '__main__':
    s = input()
    if len(s) in range (0,1000):
        #using the any function that returns True if any item in an iterable are true, otherwise it returns False
        #also using a loop to check all the characters in the string
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isdigit() for c in s))
        print(any(c.islower() for c in s))
        print(any(c.isupper() for c in s))
