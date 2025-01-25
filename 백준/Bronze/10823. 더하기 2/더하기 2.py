import sys

def main():
    s = ''.join(s.strip() for s in sys.stdin.readlines())
    return sum(map(int, s.split(',')))

if __name__ == "__main__":
    print(main())
