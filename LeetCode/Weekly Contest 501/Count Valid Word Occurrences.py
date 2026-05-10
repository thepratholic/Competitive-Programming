from typing import Counter


class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = ''.join(chunks)

        words = []
        cur = ""

        for i, ch in enumerate(s):
            if ch.islower():
                cur += ch

            elif ch == '-':
                prev = i > 0 and s[i - 1].islower()

                nxt = i + 1 < len(s) and s[i + 1].islower()

                if prev and nxt:
                    cur += ch
                
                else:
                    if cur:
                        words.append(cur)
                    cur = ""

            else:
                if cur:
                    words.append(cur)
                cur = ""

        if cur:
            words.append(cur)

        f = Counter(words)

        return [f[q] for q in queries]