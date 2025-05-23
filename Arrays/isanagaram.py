class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # handles edge case
        if len(s) != len(t):
            return False
        # initialize count with 26 index for the alphabets
        count = [0] * 26
        for i in range(len(s)):
            # counts the frequency in s
            count[ord(s[i]) - ord('a')] += 1
            # decrement the frequency in t
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True

# time complexity: O(nlogn + mlogm) nth element in s and mth element in t
# space complexity: O(1)

# alternative implementation

#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        if len(s) != len(t):
#            return False
#
#        countS, countT = {}, {}
#
#        for i in range(len(s)):
#            countS[s[i]] = 1 + countS.get(s[i], 0)
#            countT[t[i]] = 1 + countT.get(t[i], 0)
#        return countS == countT
