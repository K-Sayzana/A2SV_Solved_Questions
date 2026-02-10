class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return []
        
        i=(num-2)//3
        return [i, i+1, i+2]
        
