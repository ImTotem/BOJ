import sys
input = lambda: sys.stdin.readline().strip()

def main():
    s, n = input().split()
    s = int(s)
    seg = [
        [' - ', '| |', '   ', '| |', ' - '], # 0
        ['   ', '  |', '   ', '  |', '   '], # 1
        [' - ', '  |', ' - ', '|  ', ' - '], # 2
        [' - ', '  |', ' - ', '  |', ' - '], # 3
        ['   ', '| |', ' - ', '  |', '   '], # 4
        [' - ', '|  ', ' - ', '  |', ' - '], # 5
        [' - ', '|  ', ' - ', '| |', ' - '], # 6
        [' - ', '  |', '   ', '  |', '   '], # 7
        [' - ', '| |', ' - ', '| |', ' - '], # 8
        [' - ', '| |', ' - ', '  |', ' - '], # 9
    ]

    ans = []

    for h in range(5):
        line = []
        for x in n:
            target = seg[int(x)][h]
            if target == ' - ':
                line.append(target.replace('-', '-'*s))
            elif target == '| |':
                line.append(target.replace(' ', ' '*s))
            elif target == '   ':
                line.append(' ' * (s + 2))
            elif target == '  |':
                line.append(' ' * (s + 1) + '|')
            elif target == '|  ':
                line.append('|' + ' ' * (s + 1))

        ans.append(' '.join(line))

        if h in {1, 3}:
            for _ in range(s-1):
                ans.append(' '.join(line))
    
    return '\n'.join(ans)
    

if __name__ == "__main__":
    print(main())
