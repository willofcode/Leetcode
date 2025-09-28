class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # the problem require to remove duplicated element in place in a sorted
        # array, it is also required to consider that the number k unique element
        # will be returned.
        # ex: nums = [ 1,1,1,2,2,3]
        # updated nums = [1,2,3], k = 3
        # the best approach for this problem is to implement a two pointer
        # the first pointer will keep track of unique elements,
        # the second pointer will scan the sorted elements for unique elements
        # hence determining if the curr and prev element is a duplicate
        # it is important to acknowledge the edge case and where the pointer will
        # be positioned to avoid scanning out of bound
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
        
        # time complexity: O(n) for n element in nums
        # space complexity: O(1) no additional space was used 
