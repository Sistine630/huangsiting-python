"""记数问题 | NC16538
https://ac.nowcoder.com/acm/problem/16538
遍历1到n的十进制表示，统计目标数字。
"""

import sys
n, digit = sys.stdin.buffer.read().split()
print(sum(str(value).count(digit.decode()) for value in range(1, int(n) + 1)))
