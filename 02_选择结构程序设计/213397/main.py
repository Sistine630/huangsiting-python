"""C Simple math problem | NC213397
https://ac.nowcoder.com/acm/problem/213397
判断的是X能否整除Y。
"""

import sys
x, y = map(int, sys.stdin.buffer.read().split())
print(x + y if y % x == 0 else y - x)
