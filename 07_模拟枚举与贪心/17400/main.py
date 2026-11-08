"""gpa | NC17400
https://ac.nowcoder.com/acm/problem/17400
二分加权平均分；最多删除k门时，可以取恰好保留n-k门的最优解。
"""

import sys

def highest_score(credits, scores, keep):
    low, high = float(min(scores)), float(max(scores))
    # 误差远小于题目要求的1e-5。
    for _ in range(45):
        middle = (low + high) / 2
        gains = sorted((credit * (score - middle)
                        for credit, score in zip(credits, scores)), reverse=True)
        if sum(gains[:keep]) >= 0:
            low = middle
        else:
            high = middle
    return low

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, remove = data[:2]
    credits = data[2:2 + n]
    scores = data[2 + n:2 + 2 * n]
    print(f"{highest_score(credits, scores, n - remove):.10f}")

if __name__ == "__main__":
    main()
