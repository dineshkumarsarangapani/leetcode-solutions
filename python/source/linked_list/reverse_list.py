# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from python.source.linked_list.linked_list import ListNode


def print_node(node):
    if not node:
        return
    print(">>>>>>>>>>")
    if node is not None:
        print(node.val)

    while node.next is not None:
        node = node.next
        print(node.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            current_node = head
            head = head.next
            current_node.next = prev
            prev = current_node

        return prev


class RecursiveSolution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)


if __name__ == '__main__':
    head = ListNode(10)
    first = ListNode(20)
    head.next = first
    second = ListNode(30)
    first.next = second
    second.next = ListNode(40)
    print_node(head)
    s = RecurrsiveSolution()
    sol = s.reverseList(head)
    print_node(sol)
