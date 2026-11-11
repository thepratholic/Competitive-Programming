t = int(input())
for _ in range(t):
    n, q = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    k = [int(i) for i in input().split()]

    d = {}
    d[n-1] = 1
    for i in range(1, n):
        cont = i*(n-i)
        d[cont] = d.get(cont, 0) + x[i] - x[i-1] - 1
        d[cont+i-1] = d.get(cont + i-1, 0) + 1
    for i in k:
        print(d.get(i, 0), end=' ')
    print()
