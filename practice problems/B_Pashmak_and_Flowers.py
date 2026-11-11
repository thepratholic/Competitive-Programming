n = int(input())

a = list(map(int, input().split()))

mini = min(a)
maxi = max(a)

if mini == maxi:
    print(0, n * (n - 1) // 2)
    

else:
    cnt_mini = a.count(mini)
    cnt_maxi = a.count(maxi)

    print(maxi - mini, cnt_maxi * cnt_mini)

