
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # implementation utilizing two pointer
        curr = list1
        i = 0

        while i < a - 1:
            curr = curr.next
            i += 1
        head = curr

        while i <= b:
            curr = curr.next
            i += 1

        head.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = curr

        return list1
        
        # Time complexity: O(m + n) m is mth number of node in a and nth number of node in b
        # space complexity: O(1)
        
        # alternate implementation for recursion
#        if a == 1 :
#            nxt = list1.next
#            list1.next = list2
#            while list2.next:
#                list2 = list2.next
#            self.mergeInBetween(nxt, 0, b - 1, list2)
#            return list1
#
#        if b == 0:
#            list2.next = list1.next
#            return list1
#
#        self.mergeInBetween(list1.next, a - 1, b - 1, list2)
#        return list1
        
        # time complexity: O(m + n) mth number of first LL and nth number of second LL
        # space complexity: O(n)


        # alternate implementation by converting into an array
        # cur = list1
        # arr = []
        # while cur:
        #     arr.append(cur)
        #     cur = cur.next
        # arr[a - 1].next = list2

        # cur = list2
        # while cur.next:
        #     cur = cur.next

        # cur.next = arr[b + 1]
        # return list1

        # time complexity : O(m + n)
        # space complexity : O(n)
