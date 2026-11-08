"""卡拉兹函数 | NC205898
https://ac.nowcoder.com/acm/problem/205898
只计算一次函数值，不迭代到1。
"""

n = int(input())
print(3 * n + 1 if n % 2 else n // 2)
