class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # # the idea is store the frequency of each element in nums
        # hash = {} # intialize hashmap
        # for i in nums: # loops through all elements in nums
        #     if i not in hash: # checks if element(key) not in hashmap
        #         hash[i] = 1 # initialize the frequency(value) for the element(key) to 1
        #     else:
        #         hash[i] += 1 # add 1 to the element(key)'s frequency(value)

        #     if hash[i] > (len(nums)/2): # checks if the element's frequency is more than
        #     # half the length of the array
        #             return i # return the element (key)

        # alternative implementation
        # nums.sort() # sort the elements
        # n = len(nums) # initialize length of array
        # return nums[n//2] # the logic takes the midpoint of length of array
        # # if element's frequency is more than half of a given array,
        # # then it should return the majority element
        
        # time complexity: O(n) for n/2 elements
        # space complexity: O(n) storing n/2 elements into hashmap

        # inorder to reduce space complexity, the boyer-moore voting algorithm
        # is another alternative implementation
        majority = None
        count = 0
        
        for num in nums:
            if count == 0:  # Reset majority when count is 0
                majority = num # initialize the current num to majority
            count += 1 if num == majority else -1
            # updates count accordingly (increment or decrement)
        # Since the problem guarantees that a majority element always exists,
        # this step can be omitted. But in general, if the guarantee is not given:
        # if nums.count(majority) > len(nums) // 2:
        return majority

        # time complexity: O(n) for n elements
        # space complexity: O(1) constant time due elements majority gets updated/ cancelled
        # at constant through out checking each elements


