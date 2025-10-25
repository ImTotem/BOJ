import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    dice = list(map(int, input().split()))
    # A B C D E F
    # 0 1 2 3 4 5

    """
      3
    4 0 1 5
      2
    """

    if n == 1: return sum(dice) - max(dice)

    one = min(dice)
    two = min(dice[i] + dice[j] for i in (0, 5) for j in range(1, 5))
    two = min(
        two,
        dice[1] + dice[2],
        dice[2] + dice[4],
        dice[4] + dice[3],
        dice[3] + dice[1],
    )
    three = min(
        min(
            dice[i] + dice[1] + dice[2],
            dice[i] + dice[2] + dice[4],
            dice[i] + dice[3] + dice[4],
            dice[i] + dice[1] + dice[3]
        )
        for i in (0, 5)
    )

    a = 4
    b = 8*n - a*3

    three *= a
    two *= b
    one *= 5*n*n - (a * 3) - (b * 2)

    return one + two + three
    
if __name__ == "__main__":
    print(main())
