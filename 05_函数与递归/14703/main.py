"""素数回文 | NC14703
https://ac.nowcoder.com/acm/problem/14703
把原数最后一位作为中点构造回文，再用试除法判断素数。
"""

import math

def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True

def main():
    digits = input().strip()
    palindrome = int(digits + digits[-2::-1])
    print("prime" if is_prime(palindrome) else "noprime")

if __name__ == "__main__":
    main()
