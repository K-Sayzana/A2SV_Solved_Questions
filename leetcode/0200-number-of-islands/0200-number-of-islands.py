class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N, M=len(grid), len(grid[0])
        visited=[[0]*M for _ in range(N)]
        count=0

        def dfs(r, c):
            stk=[(r, c)]
            visited[r][c]=1

            while stk:
                rr, cc=stk.pop()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc=rr + dx, cc + dy
                    if 0<=nr<=N-1 and 0<=nc<=M-1 and grid[nr][nc]=='1' and not visited[nr][nc]:
                        visited[nr][nc]=1
                        stk.append((nr, nc))

        visited=[[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j]=='1':
                    count+=1
                    dfs(i, j)
        

        return count