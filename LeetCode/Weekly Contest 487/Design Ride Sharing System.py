from collections import deque
from typing import List


class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.cancelled_riders = set()
        self.active_riders = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.active_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] in self.cancelled_riders:
            rider = self.riders.popleft()
            self.cancelled_riders.discard(rider)
            self.active_riders.discard(rider)

        if not self.riders or not self.drivers:
            return [-1, -1]

        driver = self.drivers.popleft()
        rider = self.riders.popleft()
        self.active_riders.discard(rider)
        return [driver, rider]
        
    def cancelRider(self, riderId: int) -> None:
        if riderId in self.active_riders:
            self.cancelled_riders.add(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)