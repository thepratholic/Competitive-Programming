def solve(N):
    queue = list(range(1, N+10))
    seconds = 0

    while True:
        seconds += 1

        first = queue[0]
        third = queue[2] if len(queue) > 2 else -1

        if first == N or third == N:
            return seconds

        queue.pop(0)
        if len(queue) > 1:
            queue.pop(1)

T = int(input())

for _ in range(T):
    N = int(input())
    print(solve(N))