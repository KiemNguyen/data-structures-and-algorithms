class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = Node(-1)
    
    # Function to insert a new node at the beginning
    def insert_at_head(self, new_data):
        # 2. Create a new node $
        # 3. Put in the data
        new_node = Node(new_data)
        # 3. Make next of new node as head:
        new_node.next = self.head.next
        # 4. Move the head to point to new Node
        self.head.next = new_node
        return self.head
        
    # Function to add a new node after a given node
    def insert_after(self, prev_node, new_data):
        # 1. Check if the given prev_node exists:
        if prev_node is None:
            print("No previous Node")
            return
        # 2. Create a new node $
        # 3. Put in the data
        new_node = Node(new_data)
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. Make next of prev_node as new_node
        prev_node.next = new_node
        
    # Function to add node at the end
    def append(self, new_data):
        # 1. Create a new node $
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
        new_node.next = None
        # 4. If the LinkedList is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        # 5. Else traverse till the last node
        last = self.head
        while last.next is not None:
            last = last.next
        # 6. Change the next of last node
        last.next = new_node

    # Function to check if the linked list is empty
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # Function to print contents of a linked list
    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return False
        temp = self.head.next
        while temp.next is not None:
            print(temp.data, "->")
            temp = temp.next
        print(temp.data, "-> None")
        return True

linked_list = LinkedList()
linked_list.print_list()

for i in range(1,10,1):
    linked_list.insert_at_head(i)
linked_list.print_list()
