from typing import List


class Solution:
    def minSplitMerge(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        s, t = tuple(a), tuple(b)
        if s == t: return 0
        f, g = {s}, {t}
        df, dg = {s: 0}, {t: 0}
        while f and g:
            if len(f) > len(g):
                f, g = g, f
                df, dg = dg, df
            nf = set()
            for st in f:
                arr = list(st)
                for L in range(n):
                    for R in range(L, n):
                        sub = arr[L:R+1]
                        rem = arr[:L] + arr[R+1:]
                        for p in range(len(rem)+1):
                            if p == L: continue
                            na = tuple(rem[:p] + sub + rem[p:])
                            if na in df: continue
                            if na in dg: return df[st] + 1 + dg[na]
                            df[na] = df[st] + 1
                            nf.add(na)
            f = nf
        return -1