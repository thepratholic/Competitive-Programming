n = int(input())

s = 0
for _ in range(n):
    x = input()
    if x == "++X" or x == "X++":
        s += 1
    if x == "--X" or x == "X--": s-=1

print(s)