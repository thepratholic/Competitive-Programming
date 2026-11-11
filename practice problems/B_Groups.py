def solve():

    n = int(input())

    mat = []

    for i in range(n):
        a = list(map(int, input().split()))
        mat.append(a)

    ans = False
    for i in range(5):
        for j in range(5):
            if i == j: continue
            c1, c2, cno = 0, 0, 0

            for k in range(n):
                if mat[k][i] == 1: c1 += 1
                if mat[k][j] == 1: c2 += 1
                if mat[k][i] == 0 and mat[k][j] == 0: cno += 1

            if c1 >= n//2 and c2 >= n//2 and cno == 0:
                ans = True
                break
    if ans:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
