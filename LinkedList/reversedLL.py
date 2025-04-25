# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we can implement a two pointer approach (iteratively) (temp is temporary node)
        # initialize the curr pointer and prev pointer
        curr = head
        prev = None # currently points to null

        while curr: # while curr is not null/ still has node
            temp = curr.next # store next node to temp
            curr.next = prev # next node after current node points to prev (null)
            prev = curr # set prev node to curr node (head)
            curr = temp # update current node to next node

        return prev # prev builts the reversed list iteratively

        # time complexity: O(n) traversal for linked list
        # space complexity: O(1) constant time not storing node into another data structure

        # alternative method (recursive)
        # if not head or not head.next: # check if linked list is empty
        #     return head # return empty list

        # new_head = self.reverseList(head.next) # recursive call for next element to store new_head
        # head.next.next = head # swap
        # head.next = None
        # return new_head

        # time complexity: O(n) travesal LL
        # space complexity: O(n) call stack frame for nth node
