#create a queue called my_orders_queue to add the orders of a restaurant and remove them from it when required. using SimpleQueue

import queue

#create a queue
my_orders_queue = queue.SimpleQueue()

#add an element 
my_orders_queue.put("Order 1")
my_orders_queue.put("Order 2")
my_orders_queue.put("Order 3")

#remove a queue
my_orders_queue.get()