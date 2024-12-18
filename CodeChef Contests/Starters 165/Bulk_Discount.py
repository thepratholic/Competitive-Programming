# cook your dish here
def minimum_cost(N, A):

    A.sort()

    total_cost = 0
    for i in range(N):
        effective_cost = max(A[i] - i, 0)
        total_cost += effective_cost

    return total_cost


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    print(minimum_cost(N, A))