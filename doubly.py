class Node:
    def __init__(self, data):
        self.data = data
        self.before = None
        self.after = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print(" This is an Empty Double Linked List")
        else:
            temp = self.head
            while temp:
                print(temp.data, "----->", end=" ")
                temp = temp.after

# Create a Double Linked List
L=DoubleLinkedList()

# Create nodes and link them
n1=Node(10)
L.head = n1 

n2=Node(20)
n2.before = n1
n1.after = n2

n3=Node(30)
n3.before=n2
n2.after=n3

n4=Node(40)
n4.before=n3
n3.after=n4

n5=Node(50)
n5.before=n4
n4.after=n5

# We Display the list
L.display()
