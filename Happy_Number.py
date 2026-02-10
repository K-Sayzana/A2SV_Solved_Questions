class Solution:

    def sum_squares(self, n):
        self.sum_=0

        while n>0:
            self.sum_+=pow(n%10, 2)
            n=n//10
        
        return self.sum_

    def isHappy(self, n: int) -> bool:
        nums=set()

        while n!=1 and n not in nums:
            nums.add(n)
            n=self.sum_squares(n)
    
        return n==1
