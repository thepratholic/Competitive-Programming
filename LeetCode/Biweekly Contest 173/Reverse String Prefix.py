class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ans = ""

        rev = s[:k]
        rev = rev[::-1]

        ans += rev
        ans += s[k:]
        return ans