from collections import defaultdict
def solve():

    a = input()
    b = input()

    mpp = {f : s for f, s in zip(a, b)}

    c = input()
    ans = ""

    for char in c:
        lower_char = char.lower()

        if lower_char in mpp:
            mapped = mpp[lower_char]

            if char.isupper():
                mapped = mapped.upper()

            ans += mapped

        else:
            ans += char

    print(ans)


if __name__ == "__main__":
    solve()