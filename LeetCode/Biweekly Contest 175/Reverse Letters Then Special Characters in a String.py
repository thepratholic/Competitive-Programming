class Solution:
    def reverseByType(self, s: str) -> str:
        n = len(s)
        letter_indices, letters = [], []
        special_indices, special = [], []

        for i, ch in enumerate(s):
            if ch.isalpha():
                letter_indices.append(i)
                letters.append(ch)

            else:
                special_indices.append(i)
                special.append(ch)

        
        ans = [''] * n
        letters = letters[::-1]
        special = special[::-1]

        for idx, ch in zip(letter_indices, letters):
            ans[idx] = ch

        for idx, ch in zip(special_indices, special):
            ans[idx] = ch

        return "".join(ans)