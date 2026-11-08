"""默契 | NC215089
https://ac.nowcoder.com/acm/problem/215089
相等时用全角感叹号，不相等时用半角感叹号。
"""

import sys
x, y = map(int, sys.stdin.buffer.read().split())
print("Tacit！" if x == y else "No Tacit!")
