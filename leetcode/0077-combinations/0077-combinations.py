class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def combs(i, ans):

            if len(ans)==k:
                res.append(ans[:])
            if len(ans)>k:
                return
            for i in range(i, n+1):
                ans.append(i)
                combs(i+1, ans)
                ans.pop()
        combs(1, [])
        return res
