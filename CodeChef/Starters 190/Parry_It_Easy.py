import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []

    for _ in range(T):
        N = int(data[idx])
        X = int(data[idx + 1])
        idx += 2

        A = list(map(int, data[idx:idx + N]))
        idx += N
        B = list(map(int, data[idx:idx + N]))
        idx += N

        min_required = [0] * (N + 1)
        min_required[N] = 0 

        for i in range(N - 1, -1, -1):
            min_required[i] = max(min_required[i + 1], A[i])

        skill = X
        parries = 0
        ok = True

        for i in range(N):
            if skill < A[i]:
                ok = False
                break
            if skill >= B[i] and (skill - 1) >= min_required[i + 1]:
                parries += 1
                skill -= 1


        results.append(str(parries) if ok else "0")

    sys.stdout.write('\n'.join(results) + '\n')

main()
