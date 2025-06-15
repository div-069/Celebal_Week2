# linkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return f"Appended '{data}' as head."
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"Appended '{data}' to the list."

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def delete_nth_node(self, n):
        if self.head is None:
            return "List is empty."
        
        if n <= 0:
            return "Index must be a positive integer."

        if n == 1:
            deleted = self.head.data
            self.head = self.head.next
            return f"Deleted node at position 1 (Value: {deleted})"

        current = self.head
        for _ in range(n - 2):
            if current.next is None:
                return "Index out of range."
            current = current.next
        
        if current.next is None:
            return "Index out of range."

        deleted = current.next.data
        current.next = current.next.next
        return f"Deleted node at position {n} (Value: {deleted})"
