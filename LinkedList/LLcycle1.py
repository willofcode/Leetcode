# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # the idea is to utilize two pointers
        # slow pointer and fast pointer
        try:
        # Instantiate two pointers where slow points to the head of the list and fast points to head.next
            slow = head
            fast = head.next
            
        # Iterate over the LL (while slow != fast)
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
                
        # If slow is ever equal to fast then the while loop condition is broken and cycle is found.
            return True
        except:
            # If fast or fast.next is None this generates an exception and return False
            return False

        # time complexity: O(N) for Nth Linked List
        # space complexity: O(1) for

        # alternative method using two pointer floyd's cycle finding algorithm

        # fast = head
        # slow = head
        
        # while fast and fast.next: # ensuring that current node and next node is not null
        #     fast = fast.next.next # update to next next node
        #     slow = slow.next # update to next node
            
        #     if fast == slow: # when overlap occurs, thus a cycle is detected
        #         return True
        # # otherwise no cycle found
        # return False
        
        # alt method using hashset

        # seen = set()
        # current = head
        # while current:
        #     if current in seen:
        #         return True
        #     seen.add(current)
        #     current = current.next
        # return False

        # time complexity: O(n) visited each node
        # space complexity: O(1) stored visited nodes
        # update
