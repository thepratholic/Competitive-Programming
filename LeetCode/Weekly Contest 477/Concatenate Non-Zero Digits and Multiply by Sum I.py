class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_n = str(n)

        x = ""
        sum_ = 0

        for ch in new_n:
            if ch != '0':
                x += ch
                sum_ += int(ch)

        return sum_ * int(x) if x else 0