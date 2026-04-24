class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N=len(bombs)
        def dist(x1, y1, x2, y2):
            return (x2-x1)**2 + (y2-y1)**2

        adj=[[] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if i != j:
                    if dist(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2]**2:
                        adj[i].append(j)
        def dfs(node):
            visited=[0] * N
            visited[i]=1

            stk=[node]
            cnt=0
            while stk:
                v=stk.pop()
                cnt+=1

                for ne in adj[v]:
                    if not visited[ne]:
                        stk.append(ne)
                        visited[ne]=1
            return cnt

        ans=0
        for i in range(N):
            ans=max(ans, dfs(i))
        

        return ans

