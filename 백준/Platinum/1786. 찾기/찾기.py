import sys
input = lambda: sys.stdin.readline().removesuffix('\n')

def main():
    t, p = input(), input()
    
    lps = [0] * len(p)
    length = 0
    i = 1
    
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    pos = []
    i = 0
    j = 0
    
    while i < len(t):
        if p[j] == t[i]:
            i += 1
            j += 1
        
        if j == len(p):
            pos.append(i - j + 1)
            j = lps[j - 1]
        
        elif i < len(t) and p[j] != t[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    result = f'{len(pos)}'
    if pos:
        result += '\n' + ' '.join(map(str, pos))
    
    return result

if __name__ == "__main__":
    print(main())
