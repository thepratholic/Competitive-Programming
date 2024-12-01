class Solution:
    def smallestNumber(self, n: int) -> int:
        num_bits = n.bit_length()
        smallest_number = (1 << num_bits) - 1

        return smallest_number if smallest_number >= n else (1 << (num_bits + 1)) - 1