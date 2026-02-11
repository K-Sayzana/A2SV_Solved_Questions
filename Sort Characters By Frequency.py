class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)

        counts=[]
        for k, v in count.items():
            counts.append((v, k))

        counts.sort(reverse=True)

        ans=[]
        for c in counts:
            for i in range(c[0]):
                ans.append(c[1])
        

        return "".join(ans)
