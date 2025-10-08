# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # non empty linked list, digits are stored in reverse order, each node contain single digits
        # the value of each nodes has a range between 0 and 9
        # clarifying questions, can the 2 LL have different length?
        # clarification, when it said reverse order, please further clarify this?
        # additionally, when handling the sum of two number that return a double digit value meaning exceeding 9, carry over the number of higher significance.
        # the carry over increment the next node

        # edge case:
        # create a condition for when a next node of one of LL reaches the end
        # while the other hasn't, pass the value of the other LL to resultant LL

        # solution idea
        # traverse both linked list simultaneously as long its not null
        # set condition to add the value of both LL
        # add the sum value in resultant LL, append new node if LL is new
        # set a condition if the sum of two value at the curr index > 9
        # split into carry or remainder
        # append the higher order value to next node in the resultant LL
        # increment index of LL
        # return the value of resultant LL
        
        # psuedocode
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            currSum = l1Val + l2Val + carry
            carry = currSum // 10
            newNode = ListNode(currSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

        # time complexity: O(max(m,n)) where m and n reprensent the m-th and n-th nodes in the LL
        # space complexity: O(1) constant time no additional space was used since answer wasn't store

        # alternative implementation
        # newNode = ListNode()
        # tempNode = newNode

        # remainder = 0

        # while l1 or l2 or remainder:
        #     val1 = l1.val if l1 else 0
        #     val2 = l2.val if l2 else 0

        #     total = val1 + val2 + remainder
        #     remainder = total // 10
        #     val = total % 10
        #     tempNode.next = ListNode(val)

        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next

        #     tempNode = tempNode.next
        
        # return newNode.next


        # alternative implementation with O(n) Space iteratively
        # add = 0
        # res_list = []
        # while l1 and l2:
        #     temp = l1.val +l2.val + add
        #     res_list.append(ListNode(temp%10))
        #     add = temp//10
        #     l1 = l1.next
        #     l2 = l2.next
        
        # while l1:
        #     temp = l1.val + add
        #     res_list.append(ListNode(temp%10))
        #     add = temp//10
        #     l1 = l1.next
        # while l2:
        #     temp = l2.val + add
        #     res_list.append(ListNode(temp%10))
        #     add = temp//10
        #     l2 = l2.next

        # if add:
        #     res_list.append(ListNode(add))

        # for i in range(len(res_list)-1):
        #     res_list[i].next = res_list[i+1]
        # return res_list[0]
