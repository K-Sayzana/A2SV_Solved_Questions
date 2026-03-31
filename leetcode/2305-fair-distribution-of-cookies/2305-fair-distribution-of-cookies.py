class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        N=len(cookies)
        taken=[0] * k

        cookies.sort()
        ans=[float('inf')]
        def solve(i):
            if i==N:
                ans[0]=min(ans[0], max(taken))
                return
            if max(taken) > ans[0]:
                return 
            
            for j in range(k):
                taken[j]+=cookies[i]
                solve(i+1)
                taken[j]-=cookies[i]
                
        solve(0)
        return ans[0]
            
                
