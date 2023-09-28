# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head):
        pass

    # def reverse_list_rec(self, head):
    #     if head.next == None:
    #         return head
    #     point = self.reverse_list_rec(head)
    #     point.next = head
    #     return point

    def reverse_list_loop(self, head):
        prev, current = None, head
        while current:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev



solution = Solution()
solution.reverse_list_loop()
