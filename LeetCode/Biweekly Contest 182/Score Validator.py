class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        cnt = 0

        for ch in events:
            if ch in ('0', '1', '2', '3', '4', '6'):
                score += int(ch)

            elif ch == 'W':
                cnt += 1

            elif ch == 'WD':
                score += 1

            elif ch == 'NB':
                score += 1


            if cnt == 10:
                break

        return [score, cnt]