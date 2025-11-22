
#class BrowserHistory:
    # stack implementation
#    def __init__(self, homepage: str):
#        self.history = [homepage]
#        self.future = []
#
#    def visit(self, url: str) -> None:
#        self.history.append(url)
#        self.future = []
#
#    def back(self, steps: int) -> str:
#        while steps and len(self.history) > 1:
#            self.future.append(self.history.pop())
#            steps -= 1
#        return self.history[-1]
#
#    def forward(self, steps: int) -> str:
#        while steps and self.future:
#            self.history.append(self.future.pop())
#            steps -= 1
#        return self.history[-1]
    
    # time complexity: O(1) for initialization and visit, O(n) for back and forward function in refrence to # of steps
    # space complexity: O(m * n) for n # of urls, and m average len of each url

class Listnode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Listnode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = Listnode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

# time complexity: O(1) init O(1) for visit(), O(min(n,steps)) forward and backward
# space complexity: O(m * n) n for # of visited Urls and m # average length of url, and # of steps forward or backward


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
