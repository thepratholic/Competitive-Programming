n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)

l = 0
while l < n and a[l] == sorted_a[l]:
    l += 1

r = n - 1
while r >= 0 and a[r] == sorted_a[r]:
    r -= 1

if l >= r: 
    print("yes")
    print(1, 1)
else:
    a[l:r+1] = a[l:r+1][::-1]
    if a == sorted_a:
        print("yes")
        print(l + 1, r + 1)
    else:
        print("no")
