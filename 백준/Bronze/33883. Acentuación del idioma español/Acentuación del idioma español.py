import sys
input = lambda:sys.stdin.readline().strip()

def main():
    s = input()

    a = [i for i in range(len(s)) if s[i] in 'aeiou']
    try:
        if s[-1] not in 'aeiouns':
            return a[-1] + 1

        return a[-2] + 1
    except:
        return -1

if __name__ == "__main__":
    print(main())