def solve():
    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()

    czs1, cos1 = s1.count("0"), s1.count("1")
    czs2, cos2 = s2.count("0"), s2.count("1")
    czs3, cos3 = s3.count("0"), s3.count("1")

    count_zeros = czs1 + czs2 + czs3
    count_ones = (n * 3) - count_zeros

    if count_zeros == 0 or count_ones == 0:
        print(0)
        return

    if count_ones % n != 0 or count_zeros % n != 0:
        print(-1)
        return

    ans = 0

    if count_zeros == n:
        ans = min(cos1, cos2, cos3)

    else:
        ans = min(czs1, czs2, czs3)

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
