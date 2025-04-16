class MinStack:

    def __init__(self):
        self.stack = [] # intialize stack
        
    def push(self, val: int) -> None:
        min_val = self.getMin() # get current min
        if min_val == None or min_val > val: # check if stack is empty or
        # the new val is smaller than min val
            min_val = val # intialize new min val = to new val
        
        self.stack.append([val, min_val]) # push pair on to the stack

    def pop(self) -> None:
        self.stack.pop() # pop element from stack
        
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None # return the first top element

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None # return second to top element

    # time complexity: O(1) for all stack operation
    # space complexity: O(n) storing n elements into the stack

    # alternative implementation

    # def __init__(self):
    #     self.stack = [ (None, float('inf')) ]
        
    # def push(self, val: int) -> None:
    #     self.stack.append( (val, min(val, self.getMin())) )

    # def pop(self) -> None:
    #     self.stack.pop()
        
    # def top(self) -> int:
    #     return self.stack[-1][0]

    # def getMin(self) -> int:
    #     return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
