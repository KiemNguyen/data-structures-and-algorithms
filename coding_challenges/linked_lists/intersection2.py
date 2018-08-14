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
        while(temp):
            print(temp.data)
            temp = temp.next
            
    # Function to find LinkedList Intersection
    def getIntersectionNode(self, headA, headB):
        curA,curB = headA,headB
        lenA,lenB = 0,0
        # Calculate length of 1st Linked List
        while curA is not None:
            lenA += 1
            curA = curA.next
        # Calculate length of 2nd Linked List
        while curB is not None:
            lenB += 1
            curB = curB.next
            
        curA,curB = headA,headB
        # Calculate the difference
        diff = abs(lenA-lenB)
        # Move diff node in the longer Linked List
        if lenA > lenB:
            for i in range(diff):
                curA = curA.next
        elif lenB > lenA:
            for i in range(diff):
                curB = curB.next
        
        # then move 1 step in both        
        while curB != curA:
            curB = curB.next
            curA = curA.next
            
        return curA
            
# Code execution starts here
if __name__ == "__main__":
          
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)

    headB = ListNode(1)
    headB.next = ListNode(6)
    headB.next = ListNode(7)

    result = LinkedList()
    result.getIntersectionNode(headA, headB)