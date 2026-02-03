# Last updated: 2/3/2026, 9:39:17 PM
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        
        # Sets to store cells reachable from each ocean
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # Queues for BFS starting from ocean borders
        p_queue = deque()
        a_queue = deque()
        
        # Add all cells on Pacific borders (top row + left column)
        for i in range(ROWS):
            p_queue.append((i, 0))
            pacific_reachable.add((i, 0))
        for j in range(COLS):
            p_queue.append((0, j))
            pacific_reachable.add((0, j))
        
        # Add all cells on Atlantic borders (bottom row + right column)
        for i in range(ROWS):
            a_queue.append((i, COLS - 1))
            atlantic_reachable.add((i, COLS - 1))
        for j in range(COLS):
            a_queue.append((ROWS - 1, j))
            atlantic_reachable.add((ROWS - 1, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(queue: deque, reachable: set):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Valid cell, not visited, and water can flow from current to neighbor (i.e., neighbor >= current)
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in reachable and
                        heights[nr][nc] >= heights[r][c]):
                        queue.append((nr, nc))
                        reachable.add((nr, nc))
        
        # Run BFS from both oceans (flowing uphill)
        bfs(p_queue, pacific_reachable)
        bfs(a_queue, atlantic_reachable)
        
        # Intersection: cells reachable from both oceans
        return list(pacific_reachable.intersection(atlantic_reachable))