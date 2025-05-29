class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ask clarifying question such as constraints
        # check if the length of two strings are equal
        # check each element of each string and store in hashmap
        # compare the frequency of each element in the two hashmap
        if len(s) != len(t): # handles edge cases when two string are of diffrent length
            return False
    
        countS, countT = {}, {} # initialize two hashmap
    
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # store key and value freq for s
            countT[t[i]] = 1 + countT.get(t[i], 0) # store key and value freq for t
        return countS == countT # validate the two string by comparison

    # Implementation with hashmap
    # time complexity : O(n + m)
    # space complexity : O(1)

# alternate implementation using hashmap with array

# def isAnagram(self, s: str, t: str) -> bool:
#     # handles edge case 
#     if len(s) != len(t):
#         return False
#     # initialize count with 26 index for the alphabets
#     count = [0] * 26
#     for i in range(len(s)):
#         # counts the frequency in s
#         count[ord(s[i]) - ord('a')] += 1
#         # decrement the frequency in t
#         count[ord(t[i]) - ord('a')] -= 1
    
#     for val in count:
#         if val != 0:
#             return False
#     return True

# time complexity: O(n + m) nth element in s and mth element in t
# space complexity: O(1)
            

# alternative implementation with sorting 
    
# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
        
#     return sorted(s) == sorted(t)

#     # time complexity : O(nlogn + mlogm) # utilizing sort increase time
#     # space complexity : O(1)
