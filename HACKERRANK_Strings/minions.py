def minion_game(string):
    upper_string = string.upper()
    vowels = 'AEIOU'
    len_str = len(upper_string)
    K_score, S_score = 0,0
    if len_str>0 and len_str< pow(10,6):
        for i in range(len_str):
            if upper_string[i] in vowels:
                K_score+= len(string)-i
            #the score is equals to the number of times a word occurs in string
            else:
                S_score+=len(string)-i
        if S_score>K_score:
            print("Stuart "+"%d" % S_score)
        elif K_score>S_score:
            print("Kevin "+"%d" % K_score)
        else:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


#subtracting the index of the found 'vowel'  gives us the number of words starting from that index with a vowel at first.