# cook your dish here
x, n = map(int, input().split())

remaining = x - (n * 10)

print(remaining // 20)