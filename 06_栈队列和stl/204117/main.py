"""牛牛的三角形 | NC204117
https://ac.nowcoder.com/acm/problem/204117
排序后检查相邻三边；存在可行三元组时必能找到相邻的可行三元组。
"""

import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    sides = sorted(data[1:1 + data[0]])
    for i in range(len(sides) - 2):
        a, b, c = sides[i:i + 3]
        if a + b > c:
            print(a, b, c)
            return
    print("No solution")

if __name__ == "__main__":
    main()
