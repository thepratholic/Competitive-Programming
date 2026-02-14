from typing import DefaultDict, List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n = len(words)
        ans = ""
        alphas = "abcdefghijklmnopqrstuvwxyz"
        mpp = DefaultDict(int)
        cnt = 0
        for i in range(len(alphas) -1 , -1, -1):
            mpp[cnt] = alphas[i]
            cnt += 1

        

        for word in words:

            s = 0
            for ch in word:
                s += weights[ord(ch) - ord('a')]

            s %= 26

            ans += mpp[s]

        return ans
            