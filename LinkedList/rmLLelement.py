# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # utilizing temp node ListNode(val =0, next= head)
        temp = ListNode(next=head) #
        curr = temp
        # single loop operation
        while curr.next: # checks if curr.next points to NULL
            if val == curr.next.val: # checks if curr.next node value = val,
                curr.next = curr.next.next # skip over the 'intended node'
            else: # if curr next node is not equal
                curr = curr.next # continue to traverse the LL

        return temp.next # return the filtered list
        
        # time complexity : O(n) traverse the linked list once in single while loop
        # space complexity: O(1)

        # alternative temp node implementation
        # temp = ListNode(0, head)
        # prev = temp

        # while prev: # iterate through the LL while it's not pointing to NULL
        #     # checks next node if its value = val and not null, skip over the unwanted node
        #     while prev.next and prev.next.val == val:
        #         prev.next = prev.next.next
        #     prev = prev.next # advance prev pointer to next node
        
        # return temp.next # return the head of the filtered list

        # alternative recursive implementation
        # Set basecase where head is None
        # if head == None:
        #     return None

        # # Set head.next to the recursive function of the next node
        # head.next = self.removeElements(head.next, val)

        # # Establish logic for each head node, such that if it's value is equal to value, set this head node to be the next node
        # if head.val == val:
        #     head = head.next
        
        # # Return the head node
        # return head

        # time complexity: O(n) recursive call until base case
        # space complexity: O(1) no store memory in a data structure

        # note: size of the pointer dependend on the architecture of the system, measured in bytes
