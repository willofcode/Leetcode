class RecentCounter:

    def __init__(self):
        # Create a new queue (double ended queue)
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Upon Ping add new ping to queue
        self.queue.append(t)

        # Remove all ping in queue with value more than 3000 away from new ping
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # Return length of queue
        return len(self.queue)

    # time complexity: O(n) for appending and removing ping
    # space complexity: O(n) for storing ping in a queue

    # Alternative implementation
    # def __init__(self):
    #     self.records = []
    #     self.start = 0

    # def ping(self, t: int) -> int:
    #     self.records.append(t)
    #     while self.records[self.start] < t - 3000:
    #         self.start += 1
    #     return len(self.records) - self.start

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# finding the most optimal solution

