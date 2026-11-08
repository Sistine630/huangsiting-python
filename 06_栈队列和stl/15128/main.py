"""老子的全排列呢 | NC15128
https://ac.nowcoder.com/acm/problem/15128
使用Python标准库替代C++ STL；按字典序输出40320个排列。
"""

import itertools
import sys
for permutation in itertools.permutations(range(1, 9)):
    sys.stdout.write(" ".join(map(str, permutation)) + "\n")
