class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # Creating the empty, solution list
        head = ListNode(0, None)
        # Temporary variable
        pointer = head

        while list1 and list2:
            if list1.val > list2.val:
                pointer.next = list1
                pointer = pointer.next

                # Move to the next Element
                list1 = list1.next
                list2 = list2.next

            elif list1.val < list2.val:
                pointer.next = list2
                pointer = pointer.next

                # Move to the next Element
                list1 = list1.next
                list2 = list2.next

            else:
                # Add the first list's element
                pointer.next = list1
                pointer = pointer.next
                pointer.next = list2
                pointer = pointer.next

                # Move to the next Element
                list1 = list1.next
                list2 = list2.next

        if list1 is None:
            pointer.next = list2
        else:
            pointer.next = list1

        return head


solution = Solution()
solution.mergeTwoLists(1, 2)
