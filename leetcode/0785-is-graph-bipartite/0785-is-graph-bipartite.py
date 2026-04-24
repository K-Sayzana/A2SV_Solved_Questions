class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        N=len(graph)

        def dfs(node):
            color=[-1] * N
            color[node]=1
            stk=[node]

            while stk:
                v=stk.pop()

                for ne in graph[v]:
                    if color[ne]!= -1 and color[ne]==color[v]:
                        return False
                    if color[ne]==-1:
                        color[ne]=1-color[v]
                        stk.append(ne)
                
            return True


        for i in range(N):
            if not dfs(i):
                return False
        

        return True