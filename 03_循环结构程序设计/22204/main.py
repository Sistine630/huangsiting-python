"""上下金字塔 | NC22204
https://ac.nowcoder.com/acm/problem/22204
读到文件尾，每个图形共2n-1行。
"""

import sys
for height in map(int, sys.stdin.buffer.read().split()):
    for row in list(range(height)) + list(range(height - 2, -1, -1)):
        print(" " * (height - row - 1) + "*" * (2 * row + 1))
