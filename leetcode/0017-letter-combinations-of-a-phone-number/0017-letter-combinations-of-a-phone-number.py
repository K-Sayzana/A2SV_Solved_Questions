class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key=['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        res=[]
        def solve(i, ans):
            if i==len(digits):
                res.append(ans)
                return
            
            for ch in key[int(digits[i])]:
                solve(i+1, ans + ch)

        solve(0, '')
        return res