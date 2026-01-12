class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)

        ans = 0

        st = set()

        for i in range(n):
            st.add(s[i])

            if len(st) == (i + 1) % 3:
                ans += 1

        return ans