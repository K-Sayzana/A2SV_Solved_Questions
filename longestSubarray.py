class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        l=0
        count=defaultdict(int)


        ans=0
        for r in range(len(nums)):
            count[nums[r]]+=1

            while count[0]>1:
                count[nums[l]]-=1
                l+=1
            
            ans=max(ans, r-l)
        

        return ans
