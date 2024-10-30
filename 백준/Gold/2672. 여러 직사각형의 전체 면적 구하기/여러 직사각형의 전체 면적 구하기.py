import sys
input = lambda:sys.stdin.readline().strip()


def main():
    n = int(input())

    rec = []
    for _ in range(n):
        x, y, w, h = tuple(map(float, input().split()))
        
        rec.append((x, y, y + h, 1)) # 사각형 시작
        rec.append((x + w, y, y + h, -1)) # 사각형 끝

    rec.sort()

    area = 0
    ys = [0] * 20000

    for i in range(len(rec) - 1):
        x, y1, y2, flag = rec[i]

        y1, y2 = int(y1 * 10), int(y2 * 10)

        for j in range(y1, y2):
            ys[j] += flag

        dx = rec[i+1][0] - x
        dy = sum(y != 0 for y in ys) / 10
        
        area += dx * dy

    if area - int(area) > 0:
        return f"{area:.2f}"
    
    return int(area)


if __name__ == "__main__":
    print(main())
