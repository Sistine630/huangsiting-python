"""数位五五 | NC22168
https://ac.nowcoder.com/acm/problem/22168
闭区间枚举；0的数位和为0，也是5的倍数。
"""

import sys

def digit_sum(number):
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total

def main():
    left, right = map(int, sys.stdin.buffer.read().split())
    print(sum(digit_sum(value) % 5 == 0 for value in range(left, right + 1)))

if __name__ == "__main__":
    main()
