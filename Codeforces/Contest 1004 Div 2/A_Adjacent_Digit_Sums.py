def can_exist(x, y):
    if y == x + 1:
        return True

    if x > y:
        diff = x - y
        k = (diff + 1) / 9
        return k > 0 and k.is_integer() and x >= 9*int(k)
    return False


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("Yes" if can_exist(x, y) else "No")