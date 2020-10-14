import re
N = int(input())
if N > 0 and N < 50:
    for _ in range(N):
        css = input()
        col_codes = re.findall(r".(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})",css) #return a list with all the matches in the css code
        if col_codes:
            print(*col_codes,sep="\n")