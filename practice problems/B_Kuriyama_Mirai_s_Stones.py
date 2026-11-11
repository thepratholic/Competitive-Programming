n = int(input())

v = list(map(int, input().split()))

m = int(input())

u = sorted(v)

prefix_v = [0] * (n + 1)
prefix_u = [0] * (n + 1)


for i in range(1, n + 1):
    prefix_v[i] = prefix_v[i-1] + v[i - 1]
    prefix_u[i] = prefix_u[i-1] + u[i - 1]

for i in range(m):
    t, l, r = map(int, input().split())

    if(t == 1):
        print(prefix_v[r] - prefix_v[l-1])

    else:
        print(prefix_u[r] - prefix_u[l-1])

