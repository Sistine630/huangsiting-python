"""从后台研发到跑路 | NC13588
https://ac.nowcoder.com/acm/problem/13588
逐字符扫描，保留字符串、转义引号、未闭合注释及原始空白。
"""

import sys

def remove_comments(source):
    output = []
    quoted = False
    i = 0
    while i < len(source):
        # 按题意，反斜杠后的引号始终只当作普通字符。
        if source[i] == "\\" and i + 1 < len(source) and source[i + 1] == '"':
            output.append(source[i:i + 2])
            i += 2
        elif source[i] == '"':
            quoted = not quoted
            output.append(source[i])
            i += 1
        elif not quoted and source.startswith("/*", i):
            end = source.find("*/", i + 2)
            if end == -1:
                output.append(source[i:])
                break
            i = end + 2
        else:
            output.append(source[i])
            i += 1
    return "".join(output)

if __name__ == "__main__":
    sys.stdout.write(remove_comments(sys.stdin.read()))
