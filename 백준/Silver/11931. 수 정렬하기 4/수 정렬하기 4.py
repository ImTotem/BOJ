import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = [int(input()) for _ in range(int(input()))]
    n.sort(reverse=True)

    return n

if __name__ == "__main__":
    print(*main(), sep="\n")