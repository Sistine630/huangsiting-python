"""数字统计 | NC16599
https://ac.nowcoder.com/acm/problem/16599
函数统计闭区间内数字2的总出现次数。
"""

import sys

def count_twos(left, right):
    return sum(str(value).count("2") for value in range(left, right + 1))

def main():
    left, right = map(int, sys.stdin.buffer.read().split())
    print(count_twos(left, right))

if __name__ == "__main__":
    main()
