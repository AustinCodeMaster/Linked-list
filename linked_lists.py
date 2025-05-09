class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, name):
        new_node = Node(name)
        # If the list is empty or the new name should be the first
        if self.head is None or self.head.data > name:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the list to find the correct position
        current = self.head
        while current.next is not None and current.next.data < name:
            current = current.next

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    names = ["Alice", "Charlie", "Bob", "Diana"]
    linked_list = LinkedList()

    for name in names:
        linked_list.insert_sorted(name)

    print("Names in alphabetical order:")
    linked_list.display()

