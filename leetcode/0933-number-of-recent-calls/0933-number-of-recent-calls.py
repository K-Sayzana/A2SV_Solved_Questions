class RecentCounter:

    def __init__(self):
        self.stack=deque()

    def ping(self, t: int) -> int:
        
        while self.stack and self.stack[0]<(t-3000):
            self.stack.popleft()
        
        self.stack.append(t)

        return len(self.stack)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)