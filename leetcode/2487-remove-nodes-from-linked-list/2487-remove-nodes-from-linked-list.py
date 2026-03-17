# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _(n):
            if not n: return None
            n.next = _(n.next)
            return n.next if n.next and n.next.val > n.val else n
        return _(head)
        