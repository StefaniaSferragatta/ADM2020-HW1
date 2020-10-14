from collections import Counter, OrderedDict

#define empty ordered dictionary to counts the occurences
dictionary = OrderedDict()
n = int(input())
if n >= 1 and n <= pow(10,5):
    for _ in range(n):
        words = str(input().strip())
        l_words = words.lower()
        #sum_len = sum(len(l_words))
        #if sum_len <= pow(10,6):
        dictionary[l_words] = dictionary.get(l_words,0)+1
    len_dict = len(dictionary)
    print (len_dict)
    val_dict = dictionary.values()
    print (*val_dict)

