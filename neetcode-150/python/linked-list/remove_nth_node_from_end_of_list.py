# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left_pointer = dummy_node
        # Now we need a gap of n nodes between Left and Right pointers.
        right_pointer = head
        while n > 0 and right_pointer:
            right_pointer = right_pointer.next
            n -= 1
        
        # Now we have to traverse the list till the right reaches the end.
        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        # List end is reached, left is point just before the node that needs to be removed, and right is at the end of the list
        left_pointer.next = left_pointer.next.next
        return dummy_node.next
