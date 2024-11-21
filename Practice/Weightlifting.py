A1, A2, B1, B2, C1, C2 = map(int, input().split())

best_squat = max(A1, A2)
best_bench_press = max(B1, B2)
best_deadlift = max(C1, C2)

total_score = best_squat + best_bench_press + best_deadlift

print(total_score)
