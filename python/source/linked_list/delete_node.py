from python.source.linked_list.linked_list import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Since it is not tail node, it could be head node.


def print_node(node):
    if node is not None:
        print(node.val)

    while node.next is not None:
        node = node.next
        print(node.val)


if __name__ == '__main__':
    head = ListNode(10)
    first = ListNode(20)
    head.next = first
    second = ListNode(30)
    first.next = second
    second.next = ListNode(40)
    print_node(head)
    print("-------")
    s = Solution()
    s.deleteNode(first)
    print_node(head)
