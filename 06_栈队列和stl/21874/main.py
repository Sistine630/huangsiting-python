"""好串 | NC21874
https://ac.nowcoder.com/acm/problem/21874
将a视为左括号、b视为右括号，用栈检查匹配。
"""

def is_good(text):
    stack = []
    for char in text:
        if char == "a":
            stack.append(char)
        elif char == "b" and stack:
            stack.pop()
        else:
            return False
    return not stack

print("Good" if is_good(input().strip()) else "Bad")
