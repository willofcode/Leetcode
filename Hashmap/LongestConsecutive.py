class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting implementation
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
        # Time complexity: O(n log n) due to sort()
        # Space complexity: O(n) or O(1) dependend on sorting algorithm

        # alternate implementation
        # numSet = set(nums)
        # longest = 0

        # for num in numSet:
        #     if (num - 1) not in numSet:
        #         length = 1
        #         while (num + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        # return longest

        # time complexity: O(n)
        # space complexity: O(n)

        # alternate implementation with hashmap
        # mp = defaultdict(int)
        # res = 0

        # for num in nums:
        #     if not mp[num]:
        #         mp[num] = mp[num - 1] + mp[num + 1] + 1
        #         mp[num - mp[num - 1]] = mp[num]
        #         mp[num + mp[num + 1]] = mp[num]
        #         res = max(res, mp[num])
        # return res

        # time complexity: O(n)
        # space complexity: O(n)
