class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=['*' for _ in range(len(s))]

        for pair in zip(s, indices):
            ans[int(pair[1])]=pair[0]

        return "".join(ans)
