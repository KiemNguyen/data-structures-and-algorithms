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

    def delete_list(self, linked_list, value):
        deleted = False
        if self.head.next is None:
            print("List is empty")
            return deleted
        # Traverse the linked list to find the value to be deleted
        current_node = linked_list.head.next
        previous_node = None
        while current_node is not None:
            # Node to be deleted is found
            if current_node.data == value:
                previous_node.next = current_node.next
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next

        if deleted is False:
            print("{} is not in the list".format(value))
        else:
            print("{} is deleted".format(value))


linked_list = LinkedList()
for i in range(1, 10, 1):
    linked_list.insert_at_head(i)

linked_list.print_list()

linked_list.delete_list(linked_list, 8)
linked_list.delete_list(linked_list, 21)

linked_list.print_list()