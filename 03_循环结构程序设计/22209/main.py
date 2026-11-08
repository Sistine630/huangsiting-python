"""字符金字塔 | NC22209
https://ac.nowcoder.com/acm/problem/22209
左半边字母递增，右半边对称递减。
"""

last = input().strip()
height = ord(last) - ord("A") + 1
for row in range(1, height + 1):
    ascending = "".join(chr(ord("A") + i) for i in range(row))
    print(" " * (height - row) + ascending + ascending[-2::-1])
