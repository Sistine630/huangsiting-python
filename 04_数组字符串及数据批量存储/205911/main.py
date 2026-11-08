"""牛牛的数学作业（题单原名：随机序列） | NC205911
https://ac.nowcoder.com/acm/problem/205911
当前题号对应极差和方差计算，方差保留三位小数。
"""

import sys

def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    answers = []
    for _ in range(next(data)):
        n = next(data)
        values = [next(data) for _ in range(n)]
        total = sum(values)
        # 用整数算出方差的分子，避免大数相减引起浮点精度损失。
        numerator = n * sum(value * value for value in values) - total * total
        denominator = n * n
        # 非负有理数精确四舍五入到三位小数。
        scaled = (2 * numerator * 1000 + denominator) // (2 * denominator)
        answers.append(f"{max(values) - min(values)} {scaled // 1000}.{scaled % 1000:03d}")
    print("\n".join(answers))

if __name__ == "__main__":
    main()
