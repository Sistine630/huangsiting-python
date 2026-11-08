"""约瑟夫环 | NC22227
https://ac.nowcoder.com/acm/problem/22227
编号从0开始，从k号报1，使用列表直接模拟。
"""

import sys
n, start, step = map(int, sys.stdin.buffer.read().split())
people = list(range(n))
position = start
while len(people) > 1:
    position = (position + step - 1) % len(people)
    people.pop(position)
print(people[0])
