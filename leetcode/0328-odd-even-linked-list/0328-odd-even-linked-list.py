# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head
        _o, _e, _h = head, head.next, head.next
        while _e and _e.next:
            _o.next = _o.next.next
            _o = _o.next
            _e.next = _o.next
            _e = _e.next
        _o.next = _h
        return head