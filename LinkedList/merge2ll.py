# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the implementation utilized the temp node to merge two linked list
        # linked list node consist of val and next
        # tail is temp node, temp is pointing to tail, the end of the linked list
        temp = tail = Listnode()
        
        while list1 and list2: # initialize the iteration over list1 and list2
            if list1.val < list2.val: # val represent the value of the node and compare
            # take the smallest value between list1 and list2
                tail.next = list1 # the end of the list in now pointing to list1 head
                list1 = list1.next # list1 points to next node
            else: # otherwise
                tail.next = list2 # the end of the list in now pointing to list2 head
                list2 = list2.next # list2 points to next node

            tail = tail.next # move the pointer to the next node
        # handles difference in LL lengths
        if list1: # if list1 is still not exhausted
            tail.next = list1 # point to the next node in list1
        else:
            tail.next = list2 # point to the next node in list2
        
        return temp.next # return to the head of mergelist, skipping temp node

        # time complexity: O(m+n) for every node combined between list1 and list2
        # space complexity: O(1) constant time not storing of data to another data structure

        # alternative implementation:
        
            
