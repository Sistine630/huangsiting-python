"""四舍五入 | NC200369
https://ac.nowcoder.com/acm/problem/200369
找到首个可进位的小数位，再向左连续舍入；全程使用字符串避免浮点误差。
"""

import sys

def maximize_score(score, attempts):
    digits = list(score)
    dot = digits.index(".")
    first = next((i for i in range(dot + 1, len(digits)) if digits[i] >= "5"), len(digits))
    end = len(digits)
    while attempts > 0 and first < end and first > dot and digits[first] >= "5":
        end = first
        attempts -= 1
        previous = first - 1
        if previous == dot:
            # 已舍入为整数，只需处理整数部分的进位。
            previous -= 1
            while previous >= 0 and digits[previous] == "9":
                digits[previous] = "0"
                previous -= 1
            if previous < 0:
                return "1" + "".join(digits[:dot])
            digits[previous] = str(int(digits[previous]) + 1)
            return "".join(digits[:dot])
        digits[previous] = str(int(digits[previous]) + 1)
        first = previous
    result = "".join(digits[:end])
    return result.rstrip("0").rstrip(".") if "." in result else result

def main():
    data = sys.stdin.read().split()
    _, attempts = map(int, data[:2])
    print(maximize_score(data[2], attempts))

if __name__ == "__main__":
    main()
