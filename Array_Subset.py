#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        
        count=defaultdict(int)
        for ele in a:
            count[ele]+=1
        
        for ele in b:
            if count[ele]==0:
                return False
            count[ele]-=1
        
        return True
    
