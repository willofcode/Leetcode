class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return true if array nums contain duplicate
        # return false if array nums is distinct
        # perhaps implement a hashset
        hash = set()
        for num in nums: # O(n)
            if num not in hash: # O(1)
                hash.add(num)
            else:
                return True
        return False
    
    # time complexity: O(n)
    # space complexity: O(n)

    # alternate implementation

    
