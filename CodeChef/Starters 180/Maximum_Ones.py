def solve():
    n, k = map(int, input().split())

    s = list(input().strip())

    while True:
        if k == 0:
            break
        for i in range(n - 1):
            if s[i] == '0' and s[i + 1] == '1':
                s[i] = '1'
        k -= 1

    print(s.count('1'))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()