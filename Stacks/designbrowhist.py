
class BrowserHistory:
    # stack implementation
    def __init__(self, homepage: str):
        # initialize homepage into the stack for visited url
        self.history = [homepage]
        # future resets for forward history, since the current page is homepage
        self.future = []

    def visit(self, url: str) -> None:
        # history gets updated, url is now at history.peek/ top of history
        self.history.append(url)
        # future resets for forward history, since the current page is at url
        self.future = []

    def back(self, steps: int) -> str:
        # condition for step counter and bounds for history of visited url
        while steps and len(self.history) > 1:
            # store future with recent visited url from history
            self.future.append(self.history.pop())
            # steps decrement until desired steps completed
            steps -= 1
            # return current url in history or top of history at the time
        return self.history[-1]

    def forward(self, steps: int) -> str:
        # condition for step counter and visited url in the forward history
        while steps and self.future:
            # store history with forward history ordered visited url
            self.history.append(self.future.pop())
            # steps decrement until desired steps completed
            steps -= 1
            # return current url in history or top of history at the time
        return self.history[-1]
    
    # time complexity: O(1) for initialization and visit, O(n) for back and forward function in refrence to # of steps
    # space complexity: O(m * n) for n # of urls, and m average len of each url


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
