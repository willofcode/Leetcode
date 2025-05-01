# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the idea to determine where tail connect to listnode that caused a cycle
        # first detect if there is a cycle in linked list
        # then determine whe position where cycle started
        # constraint constant memory

        slow = fast = head

        while fast and fast.next: # detect a cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break # exit out of while loop
        
        # if no linked list and no cycle
        if not fast and not fast.next:
            return None

        e = slow
        h = fast
        while e.next # while slow pointer next element is not null
            if e == h:
               return e
            e = e.next
            h = h.next

        # time complexity: O(n) traversing LL
        # space complexity: O(1) not stored memory

        # alternative implementation
        # slow = fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         break
        # else: return None

        # fast = head

        # while fast != slow:
        #     fast = fast.next
        #     slow = slow.next
        
        # return slow
