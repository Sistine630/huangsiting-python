"""涂小天与他的画 | NC214218
https://ac.nowcoder.com/acm/problem/214218
第一项为测试组数，n表示整个菱形的高度。
"""

import sys
data = list(map(int, sys.stdin.buffer.read().split()))
for height in data[1:1 + data[0]]:
    middle = height // 2
    for row in range(height):
        padding = abs(row - middle)
        print(" " * padding + "*" * (height - 2 * padding))
