"""Run representative samples, formatting checks, and independent small-case oracles."""
from pathlib import Path
from itertools import combinations, permutations, product
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import ast
import contextlib
import importlib.util
import io
import json
import random
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ITEMS = json.loads((ROOT / 'problems.json').read_text())
PATHS = {item['number']: ROOT / item['path'] for item in ITEMS}
checks = 0

def run(number, text):
    result = subprocess.run([sys.executable, str(PATHS[number])], input=text,
                            text=True, capture_output=True, timeout=15)
    assert result.returncode == 0, (number, result.stderr)
    return result.stdout

def equal(number, text, expected, exact=False):
    global checks
    actual = run(number, text)
    assert (actual == expected if exact else actual.rstrip('\n') == expected.rstrip('\n')), (number, text, repr(actual), repr(expected))
    checks += 1

def load(number):
    spec = importlib.util.spec_from_file_location(f'p{number}', PATHS[number])
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module

def main():
    global checks
    assert len(PATHS) == 35
    for path in PATHS.values():
        ast.parse(path.read_text())
    equal(16570, '', 'zhe\nshi\nyi\ndao\nqian\ndao\nti', exact=True)
    equal(18929, '', '4396 = 28 x 157\n5346 = 18 x 297\n5346 = 27 x 198\n5796 = 12 x 483\n5796 = 42 x 138\n6952 = 4 x 1738\n7254 = 39 x 186\n7632 = 48 x 159\n7852 = 4 x 1963')
    equal(20750, '', '     **\n     **\n************\n************\n    *  *\n    *  *\n', exact=True)
    equal(213204, '', 'Helo word!')
    table = run(22206, '').splitlines()
    assert len(table) == 9 and table[3] == '1*4= 4 2*4= 8 3*4=12 4*4=16'
    assert table[-1].endswith('9*9=81')
    checks += 1
    for text, answer in [('1 2', '<'), ('1 1', '='), ('2 1', '>')]:
        equal(212955, text, answer)
    equal(205898, '1', '4')
    equal(205898, '2', '1')
    equal(215089, '0 0', 'Tacit！')
    equal(215089, '1 10', 'No Tacit!')
    equal(214223, '36 6', 'YES')
    equal(214223, '7 3', 'NO')
    for text, answer in [('4 12', '16'), ('8 20', '12'), ('7 100000000000', '99999999993')]:
        equal(213397, text, answer)
    equal(22204, '2\n3\n', ' *\n***\n *\n  *\n ***\n*****\n ***\n  *\n', exact=True)
    equal(22208, '4', '   1\n   2   3\n   4   5   6\n   7   8   9  10\n', exact=True)
    equal(22209, 'C', '  A\n ABA\nABCBA\n', exact=True)
    equal(22209, 'A', 'A')
    equal(214218, '3\n1\n3\n5', '*\n *\n***\n *\n  *\n ***\n*****\n ***\n  *\n', exact=True)
    equal(22056, '2', '    *\n  **\n***\n  **\n    *\n', exact=True)
    equal(205911, '2\n5\n5 4 3 2 1\n7\n333 494 655 991 101 591 941', '4 2.000\n890 86075.959')
    equal(205911, '2\n2\n1000000000 999999999\n1\n-1000000000', '1 0.250\n0 0.000')
    equal(16538, '11 1', '4')
    equal(16538, '100 0', '11')
    equal(22227, '5 1 2', '3')
    equal(22227, '5 0 1', '4')
    equal(16649, '500 3\n150 300\n100 200\n470 471', '298')
    equal(16649, '10 2\n2 5\n4 8', '4')
    for text, answer in [('5\n3 4 5 6 7', 'UP'), ('8\n12 13 14 15 14 13 12 11', 'DOWN'), ('1\n8', '-1'), ('1\n0', 'UP'), ('1\n15', 'DOWN')]:
        equal(15431, text, answer)
    equal(16599, '2 22', '6')
    equal(16599, '2 100', '20')
    equal(13584, '2017 4 4\n2000 1 0', '33\n136')
    equal(13584, '2000 2 2\n1900 2 2', '71\n40')
    equal(14703, '13', 'prime')
    equal(14703, '17', 'noprime')
    equal(22168, '10 20', '2')
    equal(22168, '0 0', '1')
    equal(15756, '2\n233 233\n2333 233', '54289\n543589')
    arrangements = run(15128, '').splitlines()
    assert len(arrangements) == 40320 and len(set(arrangements)) == 40320
    assert arrangements[0] == '1 2 3 4 5 6 7 8' and arrangements[-1] == '8 7 6 5 4 3 2 1'
    assert arrangements == sorted(arrangements) and all(set(row.split()) == set('12345678') and not row.endswith(' ') for row in arrangements)
    checks += 1
    equal(14721, '2 1\n3 6\n2 8', '11')
    # Special judge: validate the chosen values, rather than one fixed triple.
    answer = list(map(int, run(204117, '5\n2 2 3 2 2').split()))
    assert len(answer) == 3 and min(answer) > 0 and 2 * max(answer) < sum(answer)
    checks += 1
    equal(204117, '3\n1 2 1', 'No solution')
    equal(16783, '3\n13 312 343', '34331213')
    equal(16783, '2\n12 121', '12121')
    equal(21874, 'ab', 'Good')
    equal(21874, 'aab', 'Bad')
    equal(21874, 'ba', 'Bad')
    equal(21874, 'acb', 'Bad')
    equal(21874, 'aababb', 'Good')
    for text, answer in [('6 1\n10.245', '10.25'), ('6 2\n10.245', '10.3'), ('3 100\n9.2', '9.2'), ('5 3\n9.999', '10'), ('6 0\n10.200', '10.2'), ('6 5\n99.500', '100')]:
        equal(200369, text, answer)
    equal(13585, '14569\n1953\n15963\n15953\n1\n13\n213', 'YES\nNO\nYES\nNO\nYES\nNO\nYES')
    text = 'a b/*666\n2333*/c" lihai/*le*/\\"/*666*/"\n/*\n'
    equal(13588, text, 'a bc" lihai/*le*/\\"/*666*/"\n/*\n', exact=True)
    equal(13588, 'a/*x*/b/**/*/c/*unclosed\n', 'ab*/c/*unclosed\n', exact=True)
    equal(14662, '1\n5 1\n1 2\n2 3\n3 4\n4 5\n5 6', '2')
    assert abs(float(run(17400, '3 1\n1 2 3\n3 2 1')) - 7 / 3) < 1e-5
    checks += 1
    # Independent exhaustive subsets test both ratio optimizers.
    rng = random.Random(630)
    shopping = load(14662).best_rounded_ratio
    gpa = load(17400).highest_score
    rounding = load(200369).maximize_score
    for _ in range(120):
        n = rng.randint(1, 7)
        items = [(rng.randint(1, 15), rng.randint(1, 30)) for _ in range(n)]
        keep = rng.randint(1, n)
        best = max(Fraction(sum(items[i][1] for i in subset), sum(items[i][0] for i in subset)) for subset in combinations(range(n), keep))
        assert shopping(items, keep) == (2 * best.numerator + best.denominator) // (2 * best.denominator)
        credits = [x[0] for x in items]
        scores = [x[1] for x in items]
        best_gpa = max(Fraction(sum(credits[i] * scores[i] for i in subset), sum(credits[i] for i in subset)) for count in range(keep, n + 1) for subset in combinations(range(n), count))
        assert abs(gpa(credits, scores, keep) - float(best_gpa)) < 1e-5
        checks += 2
    # Exhaustively explore every rounding position on short decimals.
    def brute_round(score, attempts):
        states = {Decimal(score)}
        best = max(states)
        for _ in range(attempts):
            following = set(states)
            for value in states:
                decimals = max(0, -value.as_tuple().exponent)
                for places in range(decimals):
                    following.add(value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))
            states = following
            best = max(best, max(states))
        return best
    for _ in range(200):
        score = f'{rng.randint(0, 99)}.{rng.randint(0, 9999):04d}'
        attempts = rng.randint(0, 4)
        assert Decimal(rounding(score, attempts)) == brute_round(score, attempts), (score, attempts)
        checks += 1
    print(f'PASS: 35 solutions; {checks} sample, formatting and independent oracle checks.')

if __name__ == '__main__':
    main()
