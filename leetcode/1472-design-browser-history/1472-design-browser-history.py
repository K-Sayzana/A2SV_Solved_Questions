class BrowserHistory:
    def __init__(self, homepage: str):
        self.s = [homepage]
        self.c = 0

    def visit(self, url: str) -> None:
        self.s = self.s[:self.c + 1]
        self.s.append(url)
        self.c = len(self.s) - 1

    def back(self, steps: int) -> str:
        self.c = max(0, self.c - steps)
        return self.s[self.c]

    def forward(self, steps: int) -> str:
        self.c = min(len(self.s) - 1, self.c + steps)
        return self.s[self.c]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)