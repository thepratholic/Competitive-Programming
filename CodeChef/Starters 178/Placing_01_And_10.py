def min_transitions(x, y):
    if x == y:
        return x + y
    return x + y + abs(x - y) - 1

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min_transitions(x, y))