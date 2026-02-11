class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)

        dom=nums[0]
        c=0
        for k, v in count.items():
            if v>c:
                c=v
                dom=k
        
        a=0
        b=0
    
        ans=-1
        for i in range(len(nums)):
            if nums[i]==dom:
                a+=1
            else:
                b+=1

            if a>b and c-a > (len(nums)-i-1) - (c-a):
                ans=i
                break
        

        return ans

