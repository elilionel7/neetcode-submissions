class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

            

                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dr = x + r; dc = y + c
                    
                    if 0 <= dr < m and 0 <= dc < n and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        q.append((dr,dc))
                        fresh -= 1
                    
            time += 1
        return -1 if fresh != 0 else time

        