class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def solve(i, res):
            if i == len(nums):
                ans.append(res[:])
                return
            
            res.append(nums[i])
            solve(i+1, res)
            res.pop()
            solve(i+1, res)

        solve(0, [])
        return list(set(map(tuple, ans)))


