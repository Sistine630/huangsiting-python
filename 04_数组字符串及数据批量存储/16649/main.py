"""校门外的树 | NC16649
https://ac.nowcoder.com/acm/problem/16649
0和L处都有树，施工区间包括两端。
"""

import sys
data = iter(map(int, sys.stdin.buffer.read().split()))
length, regions = next(data), next(data)
trees = [1] * (length + 1)
for _ in range(regions):
    left, right = next(data), next(data)
    for position in range(left, right + 1):
        trees[position] = 0
print(sum(trees))
