class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count=defaultdict(int)
        count[0]=1
        
        acc=0
        ans=0
        for num in nums:
            acc+=num
            ans+=count[acc%k]
            count[acc%k]+=1
        
        return ans

        
            


