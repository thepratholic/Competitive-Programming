n = int(input())
a = list(map(int, input().split()))

v = []

for i in range(n):
    if a[i] == 1:
        v.append(i + 1)

maxi = 0
for i in range(1, len(v)):
    maxi = max(maxi, v[i] - v[i - 1])

print(maxi + 1)