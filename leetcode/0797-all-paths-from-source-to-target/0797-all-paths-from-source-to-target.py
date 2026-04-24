class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        t=len(graph)-1
        ans=[]
        # print(t)
        def dfs(node, path):
            if node == t:
                ans.append(path[:])
                return
            for ne in graph[node]:
                path.append(ne)
                dfs(ne, path)
                path.pop()
        dfs(0, [0])

        return ans
