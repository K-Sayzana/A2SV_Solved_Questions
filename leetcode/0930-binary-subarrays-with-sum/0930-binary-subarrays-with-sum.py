class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=defaultdict(int)
        count[0]=1
        acc=0

        ans=0
        for r in range(len(nums)):
            acc+=nums[r]
            ans+=count[acc-goal]
            count[acc]+=1
        

        return ans