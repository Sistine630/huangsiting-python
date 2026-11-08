"""整除判断 | NC214223
https://ac.nowcoder.com/acm/problem/214223
用余数判断整除。
"""

import sys
m, n = map(int, sys.stdin.buffer.read().split())
print("YES" if m % n == 0 else "NO")
