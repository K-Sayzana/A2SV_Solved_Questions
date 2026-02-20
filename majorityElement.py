class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        

        count=defaultdict(int)

        for num in nums:
            if len(count)<3:
                count[num]+=1
            else:
                for key in count:
                    count[key]-=1
                    if count[key]==0:
                        del count[key]
        
        ans=[]
        for k in count:
            c=0
            for num in nums:
                if num==k:
                    c+=1
            if c>len(nums)//3:
                ans.append(k)
        

        return ans
