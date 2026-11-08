"""拼数 | NC16783
https://ac.nowcoder.com/acm/problem/16783
按ab与ba的大小排序，不能直接按整数大小排序。
"""

from functools import cmp_to_key
import sys

def compare(left, right):
    return (left + right < right + left) - (left + right > right + left)

def main():
    data = sys.stdin.read().split()
    numbers = data[1:1 + int(data[0])]
    numbers.sort(key=cmp_to_key(compare))
    print("".join(numbers))

if __name__ == "__main__":
    main()
