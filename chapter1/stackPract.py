#Task 1 : implement a stack with the push() operation using a singly linked list.

#create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        # Initially there won't be any node at the top of the stack
        self.top = None
        
        # Initially there will be zero elements in the stack
        self.size = 0
        
        
    def push(self, data):
        #create a new node
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            #set the create node to top node
            self.top = new_node
            #incraese the size of the stack by 1
            self.size += 1
            
#Task 2 : implement the pop() operation for a stack. 
    def pop(self):
        if self.pop is None:
            return None
        else:
            popped_node = self.top
            # Decrement the size of the stack
            self.size -= 1
            # Update the new value for the top node
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
        
