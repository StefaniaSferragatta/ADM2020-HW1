import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    max = pow(10, 10)
    if a > 1 and a < max:
        if b > 1 and b < max:
            sum_ = a + b
            diff_ = a - b
            prod_ = a * b
            print(sum_)
            print(diff_)
            print(prod_)
        else:
            print("Invalid b input. Retry")
    else:
        print ("Invalid a input. Retry")
