def ver(v):
    x = v.count('a')
    y = v.count('b')
    return (len(v) - x - y == x) or (len(v) - x - y == y)

def solve():
    s = input()

    v = [s[i] for i in range(len(s))]

    if sorted(v) == v and 'a' in v and 'b' in v and ver(v):
        print("YES")

    else:
        print("NO")

solve()    