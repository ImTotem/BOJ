import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    d = {
        'black': ('0', 1),
        'brown': ('1', 10),
        'red': ('2', 100),
        'orange': ('3', 1000),
        'yellow': ('4', 10000),
        'green': ('5', 100000),
        'blue': ('6', 1000000),
        'violet': ('7', 10000000),
        'grey': ('8', 100000000),
        'white': ('9', 1000000000)
    }
    return int(d[input()][0] + d[input()][0]) * d[input()][1]


if __name__ == "__main__":
    print(main())
