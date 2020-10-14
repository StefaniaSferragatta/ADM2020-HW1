import textwrap

def wrap(string, max_width):
    if len(string)>0 and len(string)<1000:
        if max_width>0 and max_width<len(string):
            output =  textwrap.fill(string, max_width)
            return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)