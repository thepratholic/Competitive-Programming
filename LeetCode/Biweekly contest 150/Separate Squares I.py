from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        points = []
        total_area = 0
        
        for x, y, l in squares:
            points.append((y, l, 1))  
            points.append((y + l, l, -1)) 
            total_area += l * l
        
        points.sort()
        
        curr_area = 0
        active_length = 0
        prev_y = points[0][0]
        
        for curr_y, length, change_type in points:
            curr_area += active_length * (curr_y - prev_y)
            
            if 2 * curr_area == total_area:
                return curr_y
            
            if 2 * curr_area > total_area:
                excess = 2 * curr_area - total_area
                backtrack = excess / (2 * active_length)
                return curr_y - backtrack
            
            if change_type == 1:
                active_length += length
            else:
                active_length -= length
                
            prev_y = curr_y
        
        return points[-1][0]