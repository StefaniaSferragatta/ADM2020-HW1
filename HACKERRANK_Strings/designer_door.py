N,M = map(int,input().split()) #rows and columns
if N > 5 and N < 101:
    if M > 15 and M < 303:
        #Build the UPPER PART
        for i in range(1,N//2+1): #from 1 to the middle row where "WELCOME" will be written
            #calculate number of .|. required and multiply with .|.
            pattern = (i*2-1)*".|."
            #Move the pattern to center and fill the remaining part with -
            print(pattern.center(M,"-"))
        #print the string in the center
        print("WELCOME".center(M,"-"))
        #Now build the LOWER PART (in reverse order of the upper part)
        for i in reversed(range(1,N//2+1)):
            pattern = (i*2-1)*".|."
            print(pattern.center(M,"-"))