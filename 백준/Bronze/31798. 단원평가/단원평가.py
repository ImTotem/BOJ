def main():
    a, b, c = map(int, input().split())
    if a == 0: return c*c-b
    if b == 0: return c*c-a
    return int((a+b)**.5)
print(main())