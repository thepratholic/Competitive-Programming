class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        freq = [0] * 26
        cnt = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = []

        for cur in s:
            freq[ord(cur) - ord('a')] -= 1

            while len(ans) > 0:
                last = ans[-1]

                if last > cur and (freq[ord(last) - ord('a')] > 0 or cnt[ord(last) - ord('a')] > 1):
                    ans.pop()
                    cnt[ord(last) - ord('a')] -= 1
                else:
                    break

            ans.append(cur)
            cnt[ord(cur) - ord('a')] += 1

        while len(ans) > 0:
            last = ans[-1]

            if cnt[ord(last) - ord('a')] > 1:
                ans.pop()
                cnt[ord(last) - ord('a')] -= 1

            else:
                break

        return "".join(ans)