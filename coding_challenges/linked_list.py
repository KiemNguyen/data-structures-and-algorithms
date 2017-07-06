#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:55:43 2018

@author: kiem
"""

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
    
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
        
    # Function to print contents of a linked list
    def printList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end = " ")   
            temp = temp.next
    
    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 2. Create a new node $
        # 3. Put in the data
        new_node  = Node(new_data)
        # 3. Make next of new node as head:
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node
        
    # Function to add a new node after a given node
    def insertAfter(self, prev_node, new_data):
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
        
    
        
# Code execution starts here
if __name__ == "__main__":
    
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    
    llist.printList()


        