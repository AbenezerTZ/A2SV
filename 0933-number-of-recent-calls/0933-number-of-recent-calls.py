class RecentCounter:

    def __init__(self):
        self.request = []
        self.front = 0
        self.end = 0  
    def ping(self, t: int) -> int:
        self.end += 1
        self.request.append(t)
        start = t - 3000
        while start > self.request[self.front]:
            self.front += 1
        return self.end - self.front 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)