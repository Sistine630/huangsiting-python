"""安卓图案解锁 | NC13585
https://ac.nowcoder.com/acm/problem/13585
检查重复节点和跨越的中点；题目没有要求至少四个节点。
"""

import sys

def valid_pattern(pattern):
    visited = set()
    previous = None
    for char in pattern:
        current = int(char) - 1
        if current in visited:
            return False
        if previous is not None:
            r1, c1 = divmod(previous, 3)
            r2, c2 = divmod(current, 3)
            if (r1 + r2) % 2 == 0 and (c1 + c2) % 2 == 0:
                middle = ((r1 + r2) // 2) * 3 + (c1 + c2) // 2
                if middle not in visited:
                    return False
        visited.add(current)
        previous = current
    return True

for pattern in sys.stdin.read().split():
    print("YES" if valid_pattern(pattern) else "NO")
