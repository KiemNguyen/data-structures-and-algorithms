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

    # Function to return union of list1 and list2
    def union(self, list1, list2):
        start = list1.head

        # Traverse list 1 until the end
        while start.next is not None:
            start = start.next
        # Link last element of list1 to list2
        start.next = list2.head.next
        return list1

    # Function to return intersection of list 1 and list2
    def intersection(self, list1, list2):
        result = LinkedList()
        visited_nodes = []
        l1_current = list1.head.next
        l2_current = list2.head.next

        # Traverse list1 and add unique elements in the visited_nodes list
        while l1_current is not None:
            value = l1_current.data
            if value not in visited_nodes:
                visited_nodes.append(value)
            # Traverse
            l1_current = l1_current.next

        # Traverse list2 and only add nodes in visited_nodes list
        while l2_current is not None:
            value = l2_current.data
            if value in visited_nodes:
                result.append(value)
            # Traverse
            l2_current = l2_current.next

        return result


list1 = LinkedList()
for i in range(1, 5, 1):
    list1.append(i)
list1.print_list()

list2 = LinkedList()
for i in range(3, 10, 1):
    list2.append(i)
list2.print_list()

intersec_result = LinkedList()
intersec_result.intersection(list1, list2).print_list()
