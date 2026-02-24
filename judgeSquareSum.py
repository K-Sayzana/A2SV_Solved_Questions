class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # print(ceil(sqrt(c)))

        if c==0:
            return True
        for b in range(ceil(sqrt(c))):#+1
            # print(b)
            if pow(int(sqrt(c-b*b)), 2) == (c-b*b):
                return True
        
        return False

