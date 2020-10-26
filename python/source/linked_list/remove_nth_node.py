# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from python.source.linked_list.linked_list import ListNode


def print_node(node):
    print(">>>>>>>>>>")
    if node is not None:
        print(node.val)

    while node.next is not None:
        node = node.next
        print(node.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Preserve the head to return
        dummy = ListNode(0)
        dummy.next = head
        _head = dummy
        len_list = 1
        while head.next:
            len_list += 1
            head = head.next

        req_length = len_list - n
        # reset head
        head = _head
        # loop till the nth element
        while req_length > 0:
            req_length -= 1
            head = head.next

        # simply delete that node by forgetting
        head.next = head.next.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(10)
    first = ListNode(20)
    head.next = first
    second = ListNode(30)
    first.next = second
    second.next = ListNode(40)
    print_node(head)

    s = Solution()
    h = s.removeNthFromEnd(head, 2)
    print_node(h)
