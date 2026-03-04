class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        min_l=0
        acc=0

        ans=float('-inf')
        for num in nums:
            acc+=num
            ans=max(ans, acc-min_l)
            min_l=min(min_l, acc)
        

        return ans
