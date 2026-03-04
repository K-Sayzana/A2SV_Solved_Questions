class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)

        for shift in shifts:
            if shift[2]==0:
                prefix[shift[0]]-=1
                prefix[shift[1]+1]+=1
            else:
                prefix[shift[0]]+=1
                prefix[shift[1]+1]-=1
        for i in range(1, len(s)):
            prefix[i]=prefix[i-1]+prefix[i]

        # print(prefix)
        ans=[]

        for i in range(len(s)):
            ans.append(chr((((ord(s[i])-ord('a')) + prefix[i]) % 26) +ord('a') ))

        return "".join(ans)