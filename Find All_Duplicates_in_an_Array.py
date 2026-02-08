class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        
        ans=[]
        for k, v in count.items():
            if v==2:
                ans.append(k)
        
        return ans
