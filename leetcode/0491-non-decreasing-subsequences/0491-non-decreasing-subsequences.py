class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        nums
        def solve(i, res):
            if i==len(nums):
                if len(res)>=2:
                    ans.append(res[:])
                return
            
            solve(i+1, res)
            if not res or res[-1] <= nums[i]:
                res.append(nums[i])
                solve(i+1, res)
                res.pop()
        
        solve(0, [])
        return list(set(map(tuple, ans)))
               

