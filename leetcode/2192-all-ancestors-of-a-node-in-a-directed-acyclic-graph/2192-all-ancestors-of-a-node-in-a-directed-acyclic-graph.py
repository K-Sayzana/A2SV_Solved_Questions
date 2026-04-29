class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj=[[] for _ in range(n)]

        ins=[0] * n
        for u, v in edges:
            adj[u].append(v)
            ins[v]+=1
        
        ans=[set() for _ in range(n)]

        qu=deque([i for i, cnt in enumerate(ins) if cnt==0])

        while qu:
            v=qu.popleft()

            for ne in adj[v]:
                ans[ne].add(v)
                for val in ans[v]:
                    ans[ne].add(val)
                ins[ne]-=1
                if ins[ne]==0:
                    qu.append(ne)
        for i in range(len(ans)):
            ans[i]=sorted(list(ans[i]))
        

        return ans