class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr=[0 for _ in range(50)]


        for range_ in ranges:
            for i in range(range_[0]-1, range_[1]):
                arr[i]=1
        

        return sum(arr[left-1:right])==right-left+1
        
