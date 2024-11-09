#Task 1 : Create a node and linked list

#implement a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
#implement a linkedlist       
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
#Task 2 : insert a node at the beginning of a linked list.
def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head :
        new_node.next = self.head
        self.head = new_node
    else:
        self.head = new_node
        self.tail = new_node
        
    
#Task 3:  remove a node at the beginning of a linked list.

def remove_at_beginning(self):
    self.head = self.head.next
    
