import sys
input = lambda:sys.stdin.readline().strip()

from bisect import insort_left

class Box:
    def __init__(self, length: int, width: int, height: int, x: int, y: int):
        self.length = length
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.z = 0
    
    def overlap(self, other):
        # x축 방향 겹침 검사
        if self.x + self.length <= other.x: return False
        if self.x >= other.x + other.length: return False
        # y축 방향 겹침 검사
        if self.y >= other.y + other.width: return False
        if self.y + self.width <= other.y: return False

        return True
    
    @property
    def top(self):
        return self.z + self.height
    
    def __lt__(self, other): return self.top > other.top

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}) | [{self.length}, {self.width}, {self.height}]'

    __repr__ = __str__

def main():
    lx, ly, n = map(int, input().split())
    boxes = [Box(lx, ly, 0, 0, 0)]

    for i in range(n):
        box = Box(*map(int, input().split()))
        
        for j in range(i + 1):
            if box.overlap(boxes[j]):
                box.z = boxes[j].top
                break
                
        insort_left(boxes, box)

    return boxes[0].top

if __name__ == "__main__":
    print(main())
