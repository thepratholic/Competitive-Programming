def solve():
    s = input().strip()

    cnt1, cnt0 = 0, 0

    for i in range(len(s)):
        if s[i] == '1':
            cnt1 += 1
            break

    if cnt1 == 0: 
        print("No")
        return

    for j in range(i + 1, len(s)):
        if s[j] == '0':
            cnt0 += 1


    if cnt1 > 0 and cnt0 >= 6:
        print("Yes")
        return
    else:
        print("No")
        return
    
solve()