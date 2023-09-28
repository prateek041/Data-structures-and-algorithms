class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head):
        reversed_list_head = self.reverse_and_copy_list(head)

    def reverse_and_copy_list(self, head):
        prev_new_node, current = None, head

        while current:
            new_node = ListNode(current.val)
            new_node.next = prev_new_node
            prev_new_node = new_node
            current = current.next
        return prev_new_node


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Create a linked list: 1 -> 2 -> 3 -> None
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

solution = Solution()
solution.reorder_list(node1)