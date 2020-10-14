def wrapper(f):
    def fun(l):
        l_len = len(l)
        for i in range(l_len):
            l[i] = '+91 '+l[i][-10:-5]+' '+l[i][-5:]  #+91 98756 41230
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

