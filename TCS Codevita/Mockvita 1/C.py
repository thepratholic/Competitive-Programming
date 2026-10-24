import sys


def smallest_gap(lo, hi, intervals):
    blocked = set()
    for a, b in intervals:
        blocked.update(range(a + 1, b))
    lines = [lo] + [c for c in range(lo + 1, hi) if c not in blocked] + [hi]
    return min(b - a for a, b in zip(lines, lines[1:]))


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    rects = [data[1 + 4 * i:5 + 4 * i] for i in range(n)]
    px1, py1, px2, py2 = data[1 + 4 * n:5 + 4 * n]

    width = smallest_gap(px1, px2, [(r[0], r[2]) for r in rects])
    height = smallest_gap(py1, py2, [(r[1], r[3]) for r in rects])
    print(width * height)


main()