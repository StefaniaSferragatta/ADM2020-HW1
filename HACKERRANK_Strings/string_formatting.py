def print_formatted(number):
    # your code goes here
    if number in range (1,100):
        l = len(bin(number)[2:])
        for i in range (1,n+1):
            decimal = str(i).rjust(l)
            octal = str(oct(i)[2:]).rjust(l)
            hexadecimal = hex(i)[2:].rjust(l)
            binary = bin(i)[2:].rjust(l)
            print (decimal + ' ' + octal + ' ' + hexadecimal.upper() + ' ' + binary)
    else:
        print ("Input not valid. Retry")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)