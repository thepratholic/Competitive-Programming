t = int(input())
for _ in range(t):
    n = input().strip()
    L = len(n)
    max_kept = 0
    zero_count = 0
    for ch in n:
        if ch == '0':
            zero_count += 1
        else:
            max_kept = max(max_kept, zero_count + 1)
    print(L - max_kept)
