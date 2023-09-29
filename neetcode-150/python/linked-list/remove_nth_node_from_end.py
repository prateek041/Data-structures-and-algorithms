# This code can be refined

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nodes=None):
        # Initialize the head with None
        self.head = None
        # check if nodes exist
        if len(nodes) != 0:
            # create the first element
            node = ListNode(nodes.pop(0), None)
            # Point the head to the first element.
            self.head = node
            # for every element in nodes array
            for elem in nodes:
                # previous next is the new node
                node.next = ListNode(elem, None)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Solution:
    def find_length(self, head):
        start = head
        count = 0
        while start:
            count += 1
            start = start.next
        return count

    def removeNthFromEnd(self, head, n):
        list_length = self.find_length(head)
        target = list_length-n
        count = 0
        start = head
        if target == 0:
            head = head.next
            return head
        while start:
            count += 1
            if count == target:
                temp = start.next
                if temp is None:
                    start.next = None
                else:
                    start.next = temp.next
                return head
            start = start.next


def print_list(head):
    node = head
    nodes = []
    while node is not None:
        nodes.append(str(node.val))
        node = node.next
    nodes.append("None")
    return " -> ".join(nodes)


items = [1,2]
llist = LinkedList(items)
sol = Solution()
print(sol.find_length(llist.head))
print_list(sol.removeNthFromEnd(llist.head, 2))