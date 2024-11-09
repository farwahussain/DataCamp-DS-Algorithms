#create a stack called my_book_stack to add books and remove them from it.

#import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize= 0)

#add elements to the stack
my_book_stack.put("The misunderstandings")
my_book_stack.put("Persipolis")
my_book_stack.put("The Last Question")

# Remove an element from the stack
my_book_stack.get()
