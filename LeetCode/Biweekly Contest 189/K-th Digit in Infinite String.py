class Solution:
    def kthDigit(self, k: int) -> int:
        if k <= 9:
            return k

        pref = [0]
        total_digits = 0
        first_num = 1

        for d in range(1, 17):
            cnt = first_num * 9
            total_digits += cnt * d

            pref.append(total_digits)

            first_num *= 10

        digits = 0
        for d in range(1, len(pref)):
            if pref[d] >= k:
                digits = d
                break

        k -= pref[digits - 1]

        k -= 1

        num_offset = k // digits
        digit_offset = k % digits

        first_number = 10 ** (digits - 1)

        number = first_number + num_offset

        block = number // 10

        if block % 2:
            ld = number % 10

            number = block * 10 + (9 - ld)

        return int(str(number)[digit_offset])