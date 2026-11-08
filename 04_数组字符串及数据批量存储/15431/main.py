"""比较月亮大小 | NC15431
https://ac.nowcoder.com/acm/problem/15431
先处理0和15的转折点，再看相邻两天的趋势。
"""

import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n, sizes = data[0], data[1:]
if sizes[-1] == 0:
    print("UP")
elif sizes[-1] == 15:
    print("DOWN")
elif n == 1:
    print(-1)
else:
    print("UP" if sizes[-1] > sizes[-2] else "DOWN")
