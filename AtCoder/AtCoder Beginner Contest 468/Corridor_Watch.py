def solve():
    m, d = map(int, input().split())
    s = input().strip()

    ans = 0

    for i in range(m):
        if s[i] == 'G':
            continue

        l = i
        while l >= 0 and s[l] == '.':
            l -= 1

        r = i
        while r < m and s[r] == '.':
            r += 1

        left = (l >= 0 and i - l <= d)
        right = (r < m and r - i <= d)

        if not (left or right):
            ans += 1

    print(ans)

solve()