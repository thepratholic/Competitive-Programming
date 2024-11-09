class Solution:
    def digit_product(self, x):
        product = 1
        while x > 0:
            digit = x % 10
            product *= digit
            x //= 10
        return product
    def smallestNumber(self, n: int, t: int) -> int:
        x = n
        while True:
            if self.digit_product(x) % t == 0:
                return x
            x += 1