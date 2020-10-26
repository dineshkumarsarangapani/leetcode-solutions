# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from python.source.linked_list.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow_pointer = head
        fast_pointer = head
        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                slow2 = head
                while slow2 != slow_pointer:
                    slow_pointer = slow_pointer.next
                    slow2 = slow2.next
                return slow_pointer

        return None