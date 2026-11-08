"""日历中的数字 | NC13584
https://ac.nowcoder.com/acm/problem/13584
使用标准库处理闰年，月份和日期都补足两位。
"""

import calendar
import sys

def count_digit(year, month, digit):
    days = calendar.monthrange(year, month)[1]
    return sum(f"{year:04d}-{month:02d}-{day:02d}".count(str(digit))
               for day in range(1, days + 1))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    for i in range(0, len(data), 3):
        print(count_digit(*data[i:i + 3]))

if __name__ == "__main__":
    main()
