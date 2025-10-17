def is_pal(s):
    return s == s[::-1]

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if is_pal(s):
        print(0)
        continue

    x = ''.join(c for c in s if c != '0')
    if is_pal(x):
        idx = [str(i + 1) for i, c in enumerate(s) if c == '0']
        print(len(idx))
        print(' '.join(idx))
        continue

    x = ''.join(c for c in s if c != '1')
    if is_pal(x):
        idx = [str(i + 1) for i, c in enumerate(s) if c == '1']
        print(len(idx))
        print(' '.join(idx))
        continue

    print(-1)
