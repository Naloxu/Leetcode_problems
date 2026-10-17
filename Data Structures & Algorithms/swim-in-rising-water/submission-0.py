import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(n)]
        priority_queue = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        result = 0
        
        while priority_queue:
            time, x, y = heapq.heappop(priority_queue)
            result = max(result, time)
            
            if x == n - 1 and y == n - 1:
                return result
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(priority_queue, (grid[nx][ny], nx, ny))
        
        return result