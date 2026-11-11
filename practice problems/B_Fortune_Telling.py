
def solve():
    # write per-test-case logic here
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))


    odds = sum(1 for i in a if i & 1)

    alice = x & 1
    bob = 1 - alice

    alice_end = None
    bob_end = None

    if odds & 1 == 0:
        alice_end = alice
        bob_end = bob

    else:
        alice_end = 1 - alice
        bob_end = 1 - bob

    if y & 1 == alice_end:
        print("Alice")

    else:
        print("Bob")


t = int(input())
for _ in range(t):
    solve()