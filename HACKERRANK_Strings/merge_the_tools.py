def merge_the_tools(string, k):
    #'string' is the input string
    #'k' is the length of the substring
    num_subsegments = int(len(string) / k) #divided s into len(s)/k substrings
    for index in range(num_subsegments):
        #saving the subsegment string
        subseg = string[index * k: (index + 1) * k]
        output_str = "" #empty string that will be the output
        #for every character in the subsegment
        for char in subseg:
            #appen a character if it isn't already in the output_string
            if char not in output_str:
                output_str += char
        print(output_str)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)