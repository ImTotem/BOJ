import sys
input = lambda:sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    
    acc = [0] * 55

    for i in range(1, 55):
        acc[i] = 2**(i-1) + 2*acc[i-1]
    
    def get(n):
        ret = 0
        binary = bin(n).removeprefix("0b")
        length = len(binary)

        for i in range(length):
            if int(binary[i]):
                p = length-i-1
                ret += acc[p] + (n - 2**p + 1)
                n -= 2**p
        
        return ret
    
    print(get(b) - get(a-1))

main()