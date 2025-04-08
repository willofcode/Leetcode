class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     # intialize kth largest
    #     self.k = k
    #     # the list that stores the numbers given as input (nums) when the object of KthLargest is instantiated.
    #     self.stream = nums
    #     # sort the list
    #     self.stream.sort()  # occurs once in the beginning

    # def add(self, val: int) -> int:
    #     index = self.getIndex(val)
    #     # getIndex function determine the correct index for insertion
    #     self.stream.insert(index,val)
    #     # insert val at the specified index and list is updated
    #     return self.stream[-self.k] # return the kth largest from the right
    #     # since the order is ascending -k will return the largest kth element inlist
    
    # # helper function
    # def getIndex(self, val: int) -> int: # binary search implementation O(log n)
    #     left, right = 0, len(self.stream) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         mid_element = self.stream[mid] # intialize middle
    #         if mid_element == val: # check if val is middle element
    #             return mid
    #         # Go to left half
    #         elif mid_element > val: # if val is less than middle element
    #             right = mid - 1 # right move to left by 1
    #         # Go to right half
    #         else: # val is greater than middle element
    #             left = mid + 1 # left move to right by 1
    #     return left # if left is position (index) for the insertion
        
        # time complexity: O(n^2 + n * m)
        # where m accounts for elements in nums
        # sorting accounts for O(n log n) ~ O(n^2) building up the list
        # where n accounts for adding operation

        # space complexity: O(m + n)
        # where m accounts for adding operation and growing array
        # where n stored elements in nums in stream

        # alternative implementation

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums # store nums as variable
        heapq.heapify(self.heap) # store the array into a min heap

        while len(self.heap) > k: # limit the number of element to k-elements in heap
            # remove elements until kth element to ensure kth largest
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int: # add functionality to add val (integer) into heap
        heapq.heappush(self.heap, val) # insert val to the min-heap

        if len(self.heap) > self.k: # ensure the heap size does not exceed k
            # removes and update min-heap to ensure that the root of min-heap holds the kth largest
            heapq.heappop(self.heap)

        # Return kth largest val in heap which it the root element
        return self.heap[0]

        # time complexity: O(log k) for adding and removing k elements
        # space complexity: O(k) for storing k elements in heap

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
