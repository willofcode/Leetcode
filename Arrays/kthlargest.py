class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # intialize kth largest
        self.k = k
        # the list that stores the numbers given as input (nums) when the object of KthLargest is instantiated.
        self.stream = nums
        # sort the list
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        # getIndex function determine the correct index for insertion
        self.stream.insert(index,val)
        # insert val at the specified index
        return self.stream[-self.k] # return

    def getIndex(self, val: int) -> int: # binary search implementation
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            if mid_element == val:
                return mid
            # Go to left half
            elif mid_element > val:
                right = mid - 1
            # Go to right half
            else:
                left = mid + 1
        return left

        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
