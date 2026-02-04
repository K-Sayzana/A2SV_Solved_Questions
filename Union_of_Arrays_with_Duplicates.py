class Solution:    
    def findUnion(self, a, b):
        # code here
        ans=[]
        ans.extend(a)
        ans.extend(b)
        
        return list(set(ans))
