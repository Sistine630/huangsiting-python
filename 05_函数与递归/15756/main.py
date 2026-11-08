"""233 | NC15756
https://ac.nowcoder.com/acm/problem/15756
Python整数支持任意精度，可直接计算两个长整数的乘积。
"""

import sys

def main():
    data = sys.stdin.buffer.read().split()
    cases = int(data[0])
    for i in range(cases):
        print(int(data[2 * i + 1]) * int(data[2 * i + 2]))

if __name__ == "__main__":
    main()
