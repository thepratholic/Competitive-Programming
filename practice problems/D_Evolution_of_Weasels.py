def solve(s):
    res = 'B' if s.count('B') & 1 else ''

    res += s.replace('B', '')

    while 'AA' in res or 'CC' in res:
        res = res.replace('AA', '').replace('CC', '')

    return res

if __name__ == "__main__":
    for _ in range(int(input())):
        a = input()
        b = input()

        if solve(a) == solve(b):
            print("YES")
        else:
            print("NO")
