# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2:
            if list1.val <= list2.val:
                head = ListNode(val=list1.val)
                list1 = list1.next
            else:
                head = ListNode(val=list2.val)
                list2 = list2.next
        elif list1:
            head = ListNode(val=list1.val)
            list1 = list1.next
        elif list2:
            head = ListNode(val=list2.val)
            list2 = list2.next
        else:
            return None

        curr = head
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    curr.next = ListNode(val=list1.val)
                    list1 = list1.next
                    curr = curr.next
                else:
                    curr.next = ListNode(val=list2.val)
                    list2 = list2.next
                    curr = curr.next
            elif list1:
                curr.next = ListNode(val=list1.val)
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = ListNode(val=list2.val)
                list2 = list2.next
                curr = curr.next
        
        return head

