class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.'] * n  for _ in range(n)]  
        ans=[]

        t_col=set()
        t_d1=set()
        t_d2=set()

        def solve(r):
            if r==n:
                op=[]
                for row in board:
                    op.append("".join(row))
                ans.append(op)
                return
            
            for c in range(n):
                if check(r, c):
                    t_col.add(c)
                    t_d1.add(r-c)
                    t_d2.add(r+c)

                    board[r][c]='Q'
                    solve(r+1)

                    t_col.remove(c)
                    t_d1.remove(r-c)
                    t_d2.remove(r+c)
                    board[r][c]='.'


        def check(r, c):
            if (c in t_col) or (r-c in t_d1) or (r+c in t_d2):
                return False
            
            return True
        solve(0)

        return ans
        

      