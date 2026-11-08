"""数字三角形 | NC22208
https://ac.nowcoder.com/acm/problem/22208
每个整数使用最小宽度4，数值较长时完整输出。
"""

n = int(input())
number = 1
for row in range(1, n + 1):
    print("".join(f"{value:4d}" for value in range(number, number + row)))
    number += row
