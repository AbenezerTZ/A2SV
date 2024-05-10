# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        prev = head
        even = head.next
        dhead = head
        curr = head.next.next
        flag = 0
        while curr and not flag:
            prev = curr
            if curr.next != None:
                curr = curr.next.next
            else:
                flag = 1
            even.next = prev.next
            prev.next = dhead.next
            dhead.next = prev
            even = even.next
            dhead = dhead.next
        return head
        