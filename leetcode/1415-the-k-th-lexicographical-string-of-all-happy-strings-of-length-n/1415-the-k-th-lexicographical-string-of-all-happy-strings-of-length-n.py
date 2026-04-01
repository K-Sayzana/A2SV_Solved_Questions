class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s='abc'

        res=[]
        def solve(ans):
            if len(res)==k:
                    return 
            if len(ans)==n:
                res.append("".join(ans))
                return

            for i in range(len(s)):
                if ans and s[i]==ans[-1]:
                    continue
                ans.append(s[i])
                solve( ans)
                ans.pop()
        solve([]) 
        if len(res)==k:
            return res[-1]
        else:
            return ""
    
