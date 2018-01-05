class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = Node(-1)

    # Function to add node at the end and make a circle linked list
    def append(self, new_data):
        # 1. Create a new node $
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
        new_node.next = None
        # 4. If the LinkedList is empty, then make the new node as head
        head = self.head
        if head is None:
            head = new_node
            return
        # 5. Else traverse till the last node
        while head.next is not None:
            head = head.next
        # 6. Change the next of last node
        head.next = new_node

    def insert_at_head(self, new_data):
        # 2. Create a new node
        # 3. Put in the data
        new_node = Node(new_data)
        # 3. Make next element of the new node to be the next element of the Head:
        new_node.next = self.head.next
        # 4. Make next element of the Head to be this new node
        self.head.next = new_node
        return self.head

    # Function to print contents of a linked list
    def print_list(self):
        if self.head.next is None:
            print("List is empty")
            return False
        temp = self.head.next
        while temp.next is not None:
            print(temp.data, "->", end="")
            temp = temp.next
        print(temp.data, "-> None")
        return True

    # Function to find middle value of a linked list
    def find_mid(self):
        if self.head.next is None:
            return False

        current_node = self.head.next
        # If there is only 1 element in the list, return its value
        if current_node.next is None:
            return current_node.data

        mid_node = current_node
        current_node = current_node.next.next

        while current_node is not None:
            mid_node = mid_node.next
            current_node = current_node.next
            if current_node is not None:
                current_node = current_node.next
        if mid_node is not None:
            return mid_node.data


linked_list = LinkedList()
for i in range(1,5,1):
    linked_list.insert_at_head(i)

linked_list.print_list()
print(linked_list.find_mid())
