class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end = " ")
            temp = temp.next
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        if headA is None or headB is None:
            return None
        while headA is not None:
            s.add(headA)
            headA = headA.next
            element = s.pop()
        while headB is not None and element is not None:
            if headB.data == element.data:
                return headB.data
            headB = headB.next
            
headA = LinkedList()
headB = LinkedList()

headA.push(1)
headA.push(2)
headA.push(3)
headA.push(4)
headA.push(5)
headA.push(6)
headA.push(7)
headA.push(8)
headA.push(9)
headA.push(10)
headA.push(11)
headA.push(12)
headA.push(13)
print ("First List is ") 
headA.printList()

headB.push(1)
headB.push(2)
headB.push(3)
headA.push(4)
headA.push(5)
headA.push(6)
headA.push(7)
headA.push(8)
headA.push(9)
headA.push(10)
headA.push(11)
headA.push(12)
headA.push(13)
print ('\n'"Second List is ") 
headB.printList()

result = LinkedList()
result.getIntersectionNode(headA.head, headB.head)