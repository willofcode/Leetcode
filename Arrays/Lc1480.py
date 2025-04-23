# solutin 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # we want to add each index in nums and store it in the order of the index
        res = []
        sum = 0 # initialize a sum count
        for num in nums:
            sum += num # keep track of sum
            res.append(sum) # append sum to corresponding element in nums, stored in result

        return res

        # time complexity: O(n)
        # space complexity: O(n) storing into a list

        # alternative implementation
        
        # for i in range(1,len(nums)):
        #     nums[i] += nums[i-1]
        
        # return nums

        # time complexity: O(n)
        # space complexity: O(1) constant time no additional memeory required
