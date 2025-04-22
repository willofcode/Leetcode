
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer approach [for arrays]
        # have a left and right pointer
        # area is defined by lenght * width
        # the diff of left and right pointer initalize the width
        # the container height are defined by the second tallest height
        l, r, = 0, len(height) -1
        area = 0
        while l < r: # creates a loop that doesn't overlap the midpoint
            currW = r - l
            currH = min(height[l],height[r])
            area = max(area, currH * currW) # Area gets updated frequently to determine max area

            if height[l] < height[r]: # iterator
                l += 1
            else:
                r -= 1
        return area

    # time complexity : O(N) check nth lenght of the array height
    # space complexity : O(1) constant time, nothing is being stored in a data structure
