class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m=len(board), len(board[0])
        dxns=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited=[[0]* m for _ in range(n)]

        def ff(r, c):

            board[r][c]='X'
            stk=[(r, c)]

            while stk:
                rr, cc=stk.pop()
                for dx, dy in dxns:
                    nr, nc=rr+dx, cc+dy
                    if 0<=nr<=n-1 and 0<=nc<=m-1 and board[nr][nc]=='O':
                        board[nr][nc]='X'
                        stk.append((nr, nc))

      
        def dfs(r, c):
            visited[r][c]=1
            stk=[(r, c)]
            flag=1
            while stk:
                rr, cc=stk.pop()

                if rr==0 or cc==0 or rr==n-1 or cc==m-1:
                    flag= 0

                for dx, dy in dxns:
                    nr, nc=rr+dx, cc+dy
                    if 0<=nr<=n-1 and 0<=nc<=m-1 and board[nr][nc]=='O' and not visited[nr][nc]:
                        visited[nr][nc]=1
                        stk.append((nr, nc))

            return flag
        
        ans=[]

        for i in range(n):
            for j in range(m):
                if board[i][j]=='O' and (not visited[i][j]) and dfs(i, j):
                    ans.append((i, j))
        
        for a in ans:
            ff(a[0], a[1])
        
