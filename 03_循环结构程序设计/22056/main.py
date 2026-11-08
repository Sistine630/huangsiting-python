"""箭形图案 | NC22056
https://ac.nowcoder.com/acm/problem/22056
图案共2n+1行，每向外一行多两个前导空格。
"""

import sys
for n in map(int, sys.stdin.buffer.read().split()):
    for row in range(2 * n + 1):
        offset = abs(row - n)
        print(" " * (2 * offset) + "*" * (n + 1 - offset))
