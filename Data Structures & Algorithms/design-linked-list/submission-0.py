class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        pointer = 0
        curr = self.head
        while pointer < index:
            curr = curr.next
            pointer += 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        if self.tail:
            self.head.prev = ListNode(val=val, next=self.head)
            self.head = self.head.prev
        else:
            self.head = self.tail = ListNode(val=val)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head:
            self.tail.next = ListNode(val=val, prev=self.tail)
            self.tail = self.tail.next
        else:
            self.head = self.tail = ListNode(val=val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        pointer = 0
        while pointer < index - 1:
            curr = curr.next
            pointer += 1
        new_node = ListNode(val, prev=curr, next=curr.next)
        curr.next.prev = new_node
        curr.next = new_node
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        curr = self.head
        pointer = 0
        while pointer < index:
            curr = curr.next
            pointer += 1
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)