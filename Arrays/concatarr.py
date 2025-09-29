class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # # we want the dynamic array of ans with size 2n
        # # where ans[i + n] == nums[i]
        # # idea is simple, since arr in python are dynamic
        # # append each element in nums in two iteration
        # n = len(nums)
        # ans = []

        # for i in range(n):
        #     ans.append(nums[i])
        
        # for i in range(n):
        #     ans.append(nums[i])
        
        # return ans
        # time complexity: O(n)
        # space complexity: O(n) for output array

        # alternative method with nested loop (2 pass)
        # n = 2
        # ans = []
        # for i in range(n):
        #     for num in nums:
        #         ans.append(num)
        
        # return ans
        # time complexity: O(n)
        # space complexity: O(n) for output array
        
        # alternate method with one pass
        # n = len(nums)
        # ans = [0] * (2 * n)
        # for i, num in enumerate(nums):
        #     ans[i] = ans[i+n] = num
        # return ans

        # time complexity: O(n)
        # space complexity: O(n)

        # alternate method with one pass
        n = len(nums)
        ans = [0, 0] * n
        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        return ans

        # time complexity: O(n)
        # space complexity: O(n)

            




