def solve():
    s = list(input())


    for i in range(len(s)):
        if s[i] == '?':
            prev = 'd' if i == 0 else s[i-1]
            nxt = 'e' if i+1 >= len(s) else s[i+1]
            for x in ['a', 'b', 'c']:
                if (x != prev) and (x != nxt):
                    s[i] = x
                    break


    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            print("-1")
            return

    print("".join(s))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()