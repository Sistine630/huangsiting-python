"""小咪买东西 | NC14662
https://ac.nowcoder.com/acm/problem/14662
总价值/总花费不能按单件比值贪心；二分舍入答案，用收益排序判定。
"""

import sys

def best_rounded_ratio(items, count):
    # 答案为最优比值四舍五入后的整数。
    # 判断最优比值是否 >= q-0.5，可完全使用整数运算。
    low, high = 0, 10001
    while low + 1 < high:
        candidate = (low + high) // 2
        gains = sorted((2 * value - (2 * candidate - 1) * cost
                        for cost, value in items), reverse=True)
        if sum(gains[:count]) >= 0:
            low = candidate
        else:
            high = candidate
    return low

def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    for _ in range(next(data)):
        n, count = next(data), next(data)
        items = [(next(data), next(data)) for _ in range(n)]
        print(best_rounded_ratio(items, count))

if __name__ == "__main__":
    main()
