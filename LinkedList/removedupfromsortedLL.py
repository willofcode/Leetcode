# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the linked list already sorted
        # the idea is check if next element value is equal to current element value
        # if it's equal, next element point to next next element, otherwise point to next element
        # res is a pointer to head of linked list
        res = head

        while head and head.next: # while the LL does not point to NULL (None)
            if head.val == head.next.val: # compares to check for duplicate in next element
                head.next = head.next.next. # skipping the next element to next next element
            else: # if next element is not a duplicate
                head = head.next # point to next element
        
        return res # return the new modified List

        # time complexity : O(n) traversing nth node of the linked list
        # space complexity : O(1) no space was used

        # alternate implementation using two pointer
        # # Establish two pointers
        # prev = curr = head
        
        # # While two pointers are not null
        # while curr:
        #     # Re-assign 'next' of each node to a node with a different value
        #     while curr and prev.val == curr.val:
        #         curr = curr.next
        #     prev.next = curr
            
        #     # Move both pointers to the node with a different value
        #     prev = curr
        
        # # Return the head node
        # return head

        # time complexity, space complexity = O(n), O(1)
