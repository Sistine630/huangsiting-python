"""比大小 | NC212955
https://ac.nowcoder.com/acm/problem/212955
分别处理小于、大于、等于。
"""

import sys
a, b = map(int, sys.stdin.buffer.read().split())
print("<" if a < b else ">" if a > b else "=")
