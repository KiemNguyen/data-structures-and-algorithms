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

    def reverse(self):
        previous_node = None
        current_node = self.head.next # First node
        next_node = None

        if current_node is None:
            print("Can not reverse an empty list")

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        # Link head node to the new first node
        self.head.next = previous_node

linked_list = LinkedList()
for i in range(1, 10, 1):
    linked_list.insert_at_head(i)

linked_list.print_list()

linked_list.reverse()

linked_list.print_list()