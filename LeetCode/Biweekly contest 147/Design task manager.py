from typing import List
import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}  # Maps taskId -> (userId, priority)
        self.priority_queue = []  # Max-heap of (-priority, -taskId, userId)
        
        
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:

        self.task_map[taskId] = (userId, priority)

        heapq.heappush(self.priority_queue, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:

        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.priority_queue, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:

        while self.priority_queue:
            priority, neg_taskId, userId = heapq.heappop(self.priority_queue)
            taskId = -neg_taskId
            if taskId in self.task_map and self.task_map[taskId][1] == -priority:
                del self.task_map[taskId]
                return userId
        return -1