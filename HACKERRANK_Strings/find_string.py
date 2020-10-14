def count_substring(string, sub_string):
    count = 0  # initialize the counter that rappresent the total number of occurrences of the substring in the original string
    # with two indexes i and j, i traverse through the length of the input string looking for the substring
    if len(string) >= 1 and len(string) <= 200:
        for i in range(len(string)):
            for j in range(i, len(string) + 1):
                if (string[i:j] == sub_string):  # if I found the substring
                    count += 1  # increment the counter
        return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)