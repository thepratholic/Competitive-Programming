class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0
        n = len(password)

        seen = set()

        for ch in password:
            if ch in seen:
                continue

            seen.add(ch)

            if 'a' <= ch <= 'z':
                ans += 1

            elif 'A' <= ch <= 'Z':
                ans += 2

            elif '0' <= ch <= '9':
                ans += 3

            else:
                ans += 5

        return ans