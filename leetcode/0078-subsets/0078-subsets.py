class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res=[]
        def combs(i, ans):
            if i==len(nums):
                res.append(ans[:])
                return
            
            combs(i+1, ans)
            ans.append(nums[i])
            combs(i+1, ans)
            ans.pop()
            
        

        combs(0, [])
        return res
