import sys
input = sys.stdin.readline

def check(fs, ft):
    for i in range(26):
        if fs[i] > ft[i]:
            return False
    return True

def solve():
    s = input().strip()
    t = input().strip()

    n = len(s)

    fs = [0] * 26
    ft = [0] * 26

    for ch in s:
        fs[ord(ch) - ord('a')] += 1

    for ch in t:
        ft[ord(ch) - ord('a')] += 1

    if not check(fs, ft):
        print("Impossible")
        return

    ans = []
    p1 = 0  

    for _ in range(len(t)):
        for j in range(26):
            if ft[j] == 0:
                continue

            if p1 < n and s[p1] == chr(ord('a') + j):
                p1 += 1
                ft[j] -= 1
                fs[j] -= 1
                ans.append(chr(ord('a') + j))
                break
            else:
                ft[j] -= 1
                if check(fs, ft):
                    ans.append(chr(ord('a') + j))
                    break
                else:
                    ft[j] += 1

    assert p1 == n

    print("".join(ans))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
