"""装进肚子 | NC14721
https://ac.nowcoder.com/acm/problem/14721
先全部安排在晚上，再取早晚收益差最大的K个。
"""

import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n, morning_count = data[:2]
morning = data[2:2 + n]
evening = data[2 + n:2 + 2 * n]
gains = sorted((a - b for a, b in zip(morning, evening)), reverse=True)
print(sum(evening) + sum(gains[:morning_count]))
