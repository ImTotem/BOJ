import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    isbn = list(input())

    w = (1, 3)
    checksum = 0

    for i in range(13):
        if isbn[i].isnumeric():
            checksum += int(isbn[i]) * w[i % 2]

    w = w[isbn.index('*') % 2]

    for i in range(10):
        if (i * w + checksum) % 10 == 0:
            return i

if __name__ == "__main__":
    print(main())
