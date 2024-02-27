# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer_one = l1
        pointer_two = l2
        carry = 0
        new_node_head = ListNode()
        pointer_three = new_node_head
        while pointer_one is not None or pointer_two is not None:
            value_one = (pointer_one.val if pointer_one else 0)
            value_two = (pointer_two.val if pointer_two else 0)
            sum = value_one + value_two + carry
            if sum >= 10:
                sum = sum%10
                carry = 1
            else : carry = 0
            newNode = ListNode(sum, None)
            pointer_three.next = newNode
            pointer_three = pointer_three.next

            pointer_one = (pointer_one.next if pointer_one else None)
            pointer_two = (pointer_two.next if pointer_two else None)
        if carry != 0:
            newNode = ListNode(1, None)
            pointer_three.next = newNode
        return new_node_head.next

