class Node:
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node
        
# class MyLinkedList:

#     def __init__(self):
#         self.head = Node(0)
#         self.tail = Node(0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, index: int) -> int:
#         curr = self.head.next
#         while curr and index > 0:
#             curr = curr.next
#             index -= 1
#         if curr and curr != self.tail and index == 0:
#             return curr.val
#         return -1

#     def addAtHead(self, val: int) -> None:
#         node, next_node, prev_node = Node(val), self.head.next, self.head
#         next_node.prev = node
#         prev_node.next = node
#         node.next = next_node
#         node.prev = prev_node
        
#     def addAtTail(self, val: int) -> None:
#         node, next_node, prev_node = Node(val), self.tail, self.tail.prev
#         next_node.prev = node
#         prev_node.next = node
#         node.next = next_node
#         node.prev = prev_node

#     def addAtIndex(self, index: int, val: int) -> None:
#         curr = self.head.next
#         while curr and index > 0:
#             curr = curr.next
#             index -= 1
#         if curr and index == 0:
#             node = Node(val)
#             next_node = curr
#             prev_node = curr.prev
#             next_node.prev = node
#             prev_node.next = node
#             node.next = next_node
#             node.prev = prev_node

#     def deleteAtIndex(self, index: int) -> None:
#         curr = self.head.next
#         while curr and index > 0:
#             curr = curr.next
#             index -= 1
#         if curr and curr != self.tail and index == 0:
#             next_node = curr.next
#             prev_node = curr.prev
        
    # time Complexity: O(n) for get, insert/remove at index, else O(1)
    # initialization, insert at tail/head
    # space complexity: O(n)

# optimal Doubly LinkedList

class MyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index: int) -> Node:
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index + 1):
                curr = curr.prev
        return curr
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1 # out of bound
        return self.getPrev(index).next.val

    def addAtHead(self, val: int):
        self.addAtIndex(0, val)
    
    def addAtTail(self, val: int):
        self.addAtIndex(self.size, val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = Node(val)
        prev_node = self.getPrev(index)
        next_node = prev_node.next
        prev_node.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = prev_node
        self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev_node = self.getPrev(index)
        curr_node = prev_node.next
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
    
    # time Complexity: O(n) for get, insert/remove at index, else O(1)
    # initialization, insert at tail/head
    # space complexity: O(n)
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
