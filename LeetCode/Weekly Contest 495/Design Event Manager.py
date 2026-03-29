from collections import defaultdict
from heapq import heappop, heappush


class EventManager:

    def __init__(self, events: list[list[int]]):
        self.id_to_pr = {}
        self.pr_to_ids = defaultdict(list)
        self.heap = []

        for id, pr in events:
            self.id_to_pr[id] = pr
            heappush(self.pr_to_ids[pr], id)
            heappush(self.heap, -pr)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        old = self.id_to_pr[eventId]


        self.id_to_pr[eventId] = newPriority
        heappush(self.pr_to_ids[newPriority], eventId)
        heappush(self.heap, -newPriority)

    def pollHighest(self) -> int:
        while self.heap:
            pr = -heappop(self.heap)

            if pr not in self.pr_to_ids:
                continue

            while self.pr_to_ids[pr]:
                event = self.pr_to_ids[pr][0]

                if event in self.id_to_pr and self.id_to_pr[event] == pr:
                    heappop(self.pr_to_ids[pr])
                    del self.id_to_pr[event]
                    return event

                else:
                    heappop(self.pr_to_ids[pr])

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()