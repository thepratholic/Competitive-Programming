def solve():
    x, y = map(int, input().split())

    k = 0
    total = 0

    while total + (k + 1) <= x + y:
        k += 1
        total += k

    target_x = (x - y + total) // 2
    target_x = max(0, min(total, target_x))

    ans = ['Y'] * k

    for w in range(k, 0, -1):
        if target_x >= w:
            ans[k - w] = 'X'
            target_x -= w

    print(''.join(ans))


t = int(input())

while t:
    solve()
    t -= 1