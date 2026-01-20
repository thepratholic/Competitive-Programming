from collections import defaultdict
import heapq


class AuctionSystem:

    def __init__(self):
        self.bids = defaultdict(dict)
        self.heaps = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[itemId][userId] = bidAmount
        heapq.heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.bids[itemId][userId] = newAmount
        heapq.heappush(self.heaps[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bids[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.bids or not self.bids[itemId]:
            return -1

        pq = self.heaps[itemId]
        cur = self.bids[itemId]

        while pq:
            amt, uid = pq[0]
            amt, uid = -amt, -uid

            if uid in cur and cur[uid] == amt:
                return uid

            heapq.heappop(pq)

        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)