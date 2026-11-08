"""乘法表 | NC22206
https://ac.nowcoder.com/acm/problem/22206
结果按两字符右对齐，乘法项之间用一个空格。
"""

for row in range(1, 10):
    print(" ".join(f"{col}*{row}={col * row:2d}" for col in range(1, row + 1)))
