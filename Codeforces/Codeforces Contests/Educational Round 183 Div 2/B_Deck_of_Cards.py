def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()

        if n == k:
            print('-' * k)
            continue

        mn, mx = 0, 0
        for c in s:
            if c == '0':
                mn += 1
                mx += 1
            elif c == '2':
                mx += 1

        ans = []
        for i in range(1, n + 1):
            ct = i <= mx
            cb = i > n - k + mn
            mt = i <= mn
            mb = i > n - k + mx

            if mt or mb:
                ans.append('-')
            elif not ct and not cb:
                ans.append('+')
            else:
                ans.append('?')
        print(''.join(ans))

solve()
