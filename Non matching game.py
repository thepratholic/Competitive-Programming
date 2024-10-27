# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    sa = input()
    sb = input()

    sa_set = list(set(sa))
    sb_set = list(set(sb))

    joint = list(set(sa_set+sb_set))
    if len(joint) == 26:
        print('NO')
    else:
        print('YES')