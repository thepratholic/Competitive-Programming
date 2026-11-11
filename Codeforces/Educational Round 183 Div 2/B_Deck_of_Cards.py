def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()

        if n == k:
            print('-' * k)
            continue

        top, bottom, both = 0, 0, 0
        for ch in s:
            if ch == '0':
                top += 1
            elif ch == '1':
                bottom += 1
            else:
                both += 1


        max_top = top + both
        max_bottom = bottom + both

        ans = []
        for i in range(1, n + 1):
            if i <= top or i >= (n - bottom) or (n == both):
                ans.append("-")
            elif i <= max_top or i >= (n - max_bottom):
                ans.append("?")
            else:
                ans.append("+")

        print("".join(ans))
        

solve()
