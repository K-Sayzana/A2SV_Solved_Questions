class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_p=float('inf')
        acc=0

        for num in nums:
            acc+=num
            min_p=min(min_p, acc)
        if min_p<1:
            return (abs(min_p)+1)
        
        return 1