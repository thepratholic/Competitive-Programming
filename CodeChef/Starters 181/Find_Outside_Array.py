import sys
input = sys.stdin.read
data = input().split()
idx = 0
T = int(data[idx])
idx += 1
out = []

for _ in range(T):
    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx+n]))
    idx += n
    s = set(a)
    a.sort()
    found = False
    candidates = [(a[0], a[0]), (a[0], a[-1]), (a[-1], a[-1])]
    for x, y in candidates:
        if (x + y) not in s:
            out.append(f"{x} {y}")
            found = True
            break
    if not found:
        out.append("-1")

print("\n".join(out))
