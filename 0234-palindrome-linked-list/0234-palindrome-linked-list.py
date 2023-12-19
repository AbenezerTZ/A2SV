# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        curr=None
        while slow:
            nxt=slow.next
            slow.next=curr
            curr=slow
            slow=nxt
        left,right=head,curr
        while right:
            if left.val!=right.val:
                return False
            else:
                left=left.next
                right=right.next
        return True

