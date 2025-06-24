class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # constraints to consider is to implement in O(n) time complexity
        # the longest consequetive sequence determines the order and sequence of integers
        # in the array, however the tricky part is that it is unsorted
        # need to create a function to determine consecutive sequence
        # then once function detects a sequence, add to a counter
        # also need to consider duplicates
    
        sequence = 0 # sequence starts at 0
        hash = set(nums) # rids duplicate but adds space complexity

        for num in hash:
            if num - 1 not in hash: # checks the prev num is not the set of numbers
                curr = num      # intialize the current number as num
                currsequence = 1   # intialize the first count for sequence
                while curr + 1 in hash: # checks in next num in set (next consecutive number) (O(n) operation)
                    curr += 1 # incremenet current number by one
                    currsequence += 1 #  increment count for sequence
                sequence = max(sequence, currsequence) # compares and find the longest sequence for consecutive

        return sequence # return the longest sequence

        # time complexity : O(n)
        # space complexity : O(n)
        # additionaly the  implementation with while loop may seem O(n*n) but in grand scheme of operations the actual operation of the algorithm scans and processed the numbers once hence the total time complexity is O(n+n) ~ 0(2n) ~ O(n)
        # implementation of nums.sort() can lower space complexity to O(1),
        # however tradeoff in time complexity, O(n log n)
        
        
        # if not nums: # edge case if array is empty
        #     return 0
        # # Sort the array
        # nums.sort()
        
        # # Keep track of current length count (current) and longest length count (longest). Both starting at 1.
        # longest_sequence = 1
        # current_sequence = 1

        # # Loop through the sorted array
        # for i in range(1, len(nums)):
        #     # skip duplicates
        #     if nums[i] == nums[i-1]:
        #         continue
            
        #     #else if current number is one more than previous number add to current sequence
        #     elif nums[i] == nums[i-1]+1:
        #         current_sequence += 1
        #     # Else set longest sequence and reset current sequence
        #     else:
        #         longest_sequence = max(longest_sequence, current_sequence)
        #         current_sequence = 1
        
        # # Return the longest sequence
        # return max(longest_sequence, current_sequence)











