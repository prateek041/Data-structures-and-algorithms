# Node class is a single node in the linked list.
class Node:
    def __init__(self, x):
        self.node = x 
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head

        while(node):
            yield node.node
            node = node.next

    def build(self, items):
        if(len(items) <= 0):
            self.head = None
            self.size = 0
            return self

        self.head = Node(items[0])
        temp_pointer = self.head
        self.size += 1
        for item in items[1:]:
            new_node = Node(item)
            temp_pointer.next = new_node
            temp_pointer = new_node
            self.size += 1
        return self


    def get_at(self, index):
        if(self.head) == None: return None
        start = self.head
        while index > 1:
            if (start == None):
                return None
            start = start.next
            index -= 1 

    def set_at(self, item, index):
        node = self.get_at(index-1)
        if (node == None): 
            return "index out of range"
        new_node = Node(item)
        if (node.next == None):
            node.next = new_node
        next_node = node.next
        new_node.next = next_node.next
        node.next = new_node

    def insert_first(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        

    def delete_first(self):
        if(self.head == None): return None
        self.head = self.head.next


    def insert_at(self, index, item):
        node = self.get_at(index-1)
        if node == None:
            return "index out of range"
        temp_node = node
        new_node = Node(item)
        new_node.next = temp_node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, index):
        prev_node = self.get_at(index-1)
        if prev_node== None: return "index out of range"
        if (prev_node.next == None): return self
        node_to_delete = prev_node.next
        prev_node.next = node_to_delete.next


    def insert_last(self, item):
        new_node = Node(item)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            last_node = self.get_at(self.size)
            last_node.next = new_node

    def delete_last(self):
        return self.delete_at(self.size)
        
