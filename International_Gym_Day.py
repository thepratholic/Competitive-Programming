import math

def min_trial_sessions(D, X, Y):
    for n in range(0, 101):
        discounted_price = X * (1 - (n * D / 100))
        
        discounted_price = max(0, discounted_price)
        
        total_cost = discounted_price + n
        
        if total_cost <= Y:
            return n

    return -1
T = int(input())

for _ in range(T):
    D, X, Y = map(int, input().split())
    print(min_trial_sessions(D, X, Y))
