#implement a class called PrinterTasks(), which will represent a simplified queue for a printer. 

#Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create a queue
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    #add a node to the queue       
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            

    #remove a node from a queue
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = self.head.next 
            # If the queue becomes empty, update the tail
            if self.head is None:
                self.tail = None
            return current_node.data
        
        # If the queue is empty, return None
        return None


    #checks if the queue has elements
    def has_elements(self):
        return self.head != None

class PrinterTasks:
    def __init__(self):
        self.queue = Queue()
        
    
    def add_document(self, document):
        # Add the document to the queue
        self.queue.enqueue(document)
        
    def print_documents(self):
        # Iterate over the queue while it has elements
        while self.queue.has_elements():
            # Remove the document from the queue
            document = self.queue.dequeue()
            print("Printing ", document)
            
#Add some documents to the queue and print them

printer_tasks = PrinterTasks()

printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")

printer_tasks.print_documents()