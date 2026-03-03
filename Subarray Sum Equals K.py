class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1

        acc=0
        ans=0
        for i in range(len(nums)):
            acc+=nums[i]
            ans+=prefix[acc-k]
            prefix[acc]+=1

        return ans
        
