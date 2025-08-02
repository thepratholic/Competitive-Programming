from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        ans = float('inf')

        landRide = []

        for i in range(len(landStartTime)):
            landRide.append((landStartTime[i], landDuration[i]))

        waterRide = []

        for i in range(len(waterStartTime)):
            waterRide.append((waterStartTime[i], waterDuration[i]))

        landRide.sort(key = lambda x : x[0])
        waterRide.sort(key = lambda x : x[0])

        for l in landRide:
            for w in waterRide:
                end_land = l[0] + l[1]
                water_start = max(end_land, w[0])
                water_end = water_start + w[1]
                ans = min(ans, water_end)


                # case 2
                end_water = w[0] + w[1]
                start_land = max(end_water, l[0])
                end_land = start_land + l[1]
                ans = min(ans, end_land)

        return ans