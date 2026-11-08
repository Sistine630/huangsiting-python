"""排列式 | NC18929
https://ac.nowcoder.com/acm/problem/18929
枚举乘数，检查九个数字恰好各出现一次，再排序输出。
"""

def main():
    equations = []
    # 乘积为四位数；较小乘数至多两位。
    for left in range(1, 100):
        for right in range(left + 1, 10000 // left + 1):
            product = left * right
            digits = f"{left}{right}{product}"
            if len(digits) == 9 and set(digits) == set("123456789"):
                equations.append((product, left, right))
    for product, left, right in sorted(equations):
        print(f"{product} = {left} x {right}")

if __name__ == "__main__":
    main()
