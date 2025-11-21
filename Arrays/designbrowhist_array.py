class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        self.history = self.history[:self.curr]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]
        
    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]
        
    # time complexity: O(1) for 

# we can design using stack, Dynamic array, and Doubly LL
'''
for stack, we can perform push and pop to maintain structure and order of browser history

for Dynamic array we can organized history in a linear order appending url visits
keeping track of the new urls and its location via indexing which is structured

for doubly linked list, we can maintain order by storing prev and next pointer to navigate
between urls, forward will move next pointer, back will return prev pointer in visited urls
'''

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
