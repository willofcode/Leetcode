class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort() # sort implementation

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
        # time complexity: O(n log n)
        # space complexity: O(n)
        
        # alternative implementation using min heap
#        count = {}
#        for num in nums:
#            count[num] = 1 + count.get(num, 0)
#
#        heap = []
#        for num in count.keys():
#            heapq.heappush(heap, (count[num], num))
#            if len(heap) > k:
#                heapq.heappop(heap)
#
#        res = []
#        for i in range(k):
#            res.append(heapq.heappop(heap)[1])
#        return res

        # time complexity: O(n log k)
        # space complexity: O(n +
        
        # alternative implementation using bucketsort
#        count = {}
#        freq = [[] for i in range(len(nums) + 1)]
#
#        for num in nums:
#            count[num] = 1 + count.get(num, 0)
#        for num, cnt in count.items():
#            freq[cnt].append(num)
#        
#        res = []
#        for i in range(len(freq) - 1, 0, -1):
#            for num in freq[i]:
#                res.append(num)
#                if len(res) == k:
#                    return res
        
        # most efficient
        # time complexity: O(n)
        # space complexity: O(n)
    
