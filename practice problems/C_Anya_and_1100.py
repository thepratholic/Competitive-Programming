def solve():
    s = list(input().strip())
    cnt = 0
    
    n = len(s)

    for i in range(len(s) - 3):
        if s[i : i + 4] == ["1", "1", "0", "0"]:
            cnt += 1
    
    q = int(input())

    for _ in range(q):
        i, v = map(int, input().split())

        i -= 1

        for j in range(i - 3, i + 1):
            if j < 0 or j >= n:
                continue

            if s[j : j + 4] == ["1", "1", "0", "0"]:
                cnt -= 1

        s[i] = str(v)
        for j in range(i - 3, i + 1):
            if j < 0 or j + 3 >= n:
                continue
            if s[j:j + 4] == ['1', '1', '0', '0']:
                cnt += 1

        print("YES" if cnt > 0 else "NO")


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()