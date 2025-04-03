class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # non empty arrays nums
        # in an array, find the element with no duplicates
        #
        # hash = set() # store in a set

        # for num in nums:
        #     if num not in hash: # if element is not in hash
        #         hash.add(num) # add element to hash
        #     else:       # if element is in hash
        #         hash.remove(num) # remove the element
       
        # return list(hash)[0] # return the single element left after cancelling out the freq

        # time complextiy: O(n) for every element
        # space complexity: O(n) for storing and removing (n/2) element in hashset

        # alternative implemnetation with reduce space complexity

        # xor logic truth table
        # 0 ^ 0 = 0
        # 0 ^ 1 = 1
        # 1 ^ 0 = 1
        # 1 ^ 1 = 0
        res = 0 # intialize result

        for num in nums:
            res ^= num # xor loigc checking current num with result and update the result
        
       # [2,2,1]
       # -> 0 ^ 2 = 2
       # -> 2 ^ 2 = 0
       # -> 0 ^ 1 = 1

        return res

        # time complexity: O(n) cheking n elements in the array
        # space complexity: O(1) no stoting of element occurs hence constant time

        
