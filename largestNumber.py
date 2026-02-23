class Solution:
    

    def largestNumber(self, nums: List[int]) -> str:

        if sum(nums)==0:
            return '0'
        def compare(a , b):
            if a + b > b+a:
                return -1
            else:
                return 1
        return "".join(sorted(list(map(str, nums)), key=cmp_to_key(compare)))
