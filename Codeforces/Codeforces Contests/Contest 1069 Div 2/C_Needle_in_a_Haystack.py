import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()

    n = len(s)
    m = len(t)
    s_arr = [ord(c) - 97 for c in s]

    freq = [0] * 26
    for ch in t:
        freq[ord(ch) - 97] += 1

    need_total = [0] * 26
    for c in s_arr:
        need_total[c] += 1

    for i in range(26):
        if need_total[i] > freq[i]:
            print("Impossible")
            return

    suff_need = [[0] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        row = suff_need[i]
        nxt = suff_need[i + 1]
        row[:] = nxt[:]
        row[s_arr[i]] += 1

    ans = []
    rem = freq[:]
    k = 0

    for _ in range(m):
        picked = -1
        for c in range(26):
            if rem[c] == 0:
                continue
            new_k = k
            if new_k < n and c == s_arr[new_k]:
                new_k += 1
            row = suff_need[new_k]
            if row[c] > rem[c] - 1:
                continue
            ok = True
            for x in range(26):
                if x == c:
                    continue
                if row[x] > rem[x]:
                    ok = False
                    break
            if ok:
                picked = c
                rem[c] -= 1
                k = new_k
                ans.append(chr(c + 97))
                break
        if picked == -1:
            print("Impossible")
            return

    if k != n:
        print("Impossible")
    else:
        print("".join(ans))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
