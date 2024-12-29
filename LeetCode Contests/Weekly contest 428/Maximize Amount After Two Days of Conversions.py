from collections import defaultdict, deque
from typing import List


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def bfs_max(graph, start):
            max_amount = defaultdict(float)
            max_amount[start] = 1.0
            queue = deque([start])
            
            while queue:
                current = queue.popleft()
                for neighbor, rate in graph[current]:
                    new_amount = max_amount[current] * rate
                    if new_amount > max_amount[neighbor]:
                        max_amount[neighbor] = new_amount
                        queue.append(neighbor)
            return max_amount

        # Build graphs for both days
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        
        for (s, t), r in zip(pairs1, rates1):
            graph1[s].append((t, r))
            graph1[t].append((s, 1 / r))
        
        for (s, t), r in zip(pairs2, rates2):
            graph2[s].append((t, r))
            graph2[t].append((s, 1 / r))
        
        # Perform BFS on day 1 graph
        max_day1 = bfs_max(graph1, initialCurrency)
        
        # Perform BFS on day 2 graph, starting from each currency obtained on day 1
        max_final = 0.0
        for currency, amount in max_day1.items():
            max_day2 = bfs_max(graph2, currency)
            max_final = max(max_final, max_day2[initialCurrency] * amount)
        
        return max_final