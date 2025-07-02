class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # initialize the hash table
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # initialize the array for 26 letters in the alphabet
            for c in s: 
                count[ord(c) - ord('a')] += 1 # increment count for each alphabet for each string in the array
            res[tuple(count)].append(s) 
        return list(res.values())

  # time complexity: O(m * n)
  # space complexity: O(m * n) storing m * n in hashmap
