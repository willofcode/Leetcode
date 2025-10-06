class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window method
        # ask clarifying questions:
        # - is there a specific constraint with time and space in terms of big-o notation?
        # keep track len of subarray :
        # - implement two pointer to keep track, spefically the sliding window technique
        # keep track of curr sum
        # check while curr sum >= target
        # [2,3,1,2,4,3]
        min_len = float('inf') # initialize infinity to represent some large num
        l = 0
        currsum = 0
        # we want to loop through the right boundary
        for r in range(len(nums)):
            currsum += nums[r]
        
        # this condition shrink windown, shifting the left boundary
        while currsum >= target:
            # updates the min_len
            if r - l + 1 < min_len:
                min_len = r - l + 1
            # otherwise adjust the left boundary
            currsum -= nums[l]
            l += 1
        
        return min_len if min_len != float("inf") else 0 # return 0 otherwise

        # time complexity: O(n) for n element in array nums
        # space complexity: O(1) no additional space utilized
