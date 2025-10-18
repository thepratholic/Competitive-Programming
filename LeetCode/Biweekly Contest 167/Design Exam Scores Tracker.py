from bisect import bisect_left, bisect_right


class ExamTracker:

    def __init__(self):
        self.time = []
        self.pref = []

    def record(self, time: int, score: int) -> None:
        self.time.append(time)
        total = score 
        if self.pref:
            total += self.pref[-1]

        self.pref.append(total)
        
    def totalScore(self, startTime: int, endTime: int) -> int:
        r = bisect_right(self.time, endTime) - 1
        if r < 0:
            return 0

        l = bisect_left(self.time, startTime)
        start = self.pref[l - 1] if l > 0 else 0
        end = self.pref[r] 

        return end - start


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)©leetcode