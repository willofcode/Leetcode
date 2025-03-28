
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can do this in two approach
        # we want to return the index of two numbers within an array
        # we can do this the brute approach method
        # implementing a nested for loop that will determine two number that will equate to the
        # the target

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]
        # # return empty list if no solution
        # return []
        
        # time complexity is O(n^2) because we are performing a nested for loop where each loop take O(n) time hence the formula would equate to O(n) * O(n)

        # space complecity is O(1) which constant because we are not using additional data structure to construct the solution

        # another methodology is to implement a hash map where we can store our solution in hashmap
        
        hashmap = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in hashmap:
                return [i,hashmap[compl]]
            hashmap[nums[i]] = i
        
        return []
        
        # time complexity: O(n)
        # space complexity: O(n)

