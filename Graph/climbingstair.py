class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive implementation
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)
        
        return dfs(0)

    # time complexity : O(2^n) for dfs on power of n
    # space complexity : O(n)
        
