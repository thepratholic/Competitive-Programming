class Solution:
    def minMoves(self, sx, sy, tx, ty):
        cnt = 0
        while tx > sx or ty > sy:
            cnt += 1
            if ty > tx:
                tx, ty = ty, tx
                sx, sy = sy, sx
            if tx == ty:
                if sx == 0:
                    tx = 0
                else:
                    ty = 0
            else:
                if tx < ty * 2:
                    tx -= ty
                else:
                    if tx % 2:
                        return -1
                    tx //= 2
        return -1 if tx < sx or ty < sy else cnt
