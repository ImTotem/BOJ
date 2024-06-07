import sys
input = lambda:sys.stdin.readline().strip()

def main():
    prevs = [input(), input(), input()]

    for i in range(3):
        if prevs[i].isdigit():
            n = int(prevs[i]) + 3 - i
            return "Fizz" * (not n%3) + "Buzz" * (not n%5) or n

print(main())