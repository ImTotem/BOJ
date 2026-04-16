def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    m1 = max(a)  
    m2 = max(set(a) - {m1}) if a.count(m1) == 1 else m1
    
    ans = []
    for i in range(n):
        x = [m1, m2][a[i] == m1]
        ans.append(a[i] - x)
    
    return ans
    
print(*main())