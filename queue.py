'''Python Queue library'''
#Code for creating a Queue using Nodes.

from node import Node

class Queue:
  def __init__(self, max_size=None): #initializing a Queue. 
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value): #Adding an item the Queue(always the Tail item/Node)
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
      
  # Add your dequeue method below:    
  def dequeue(self): #Removing an item from the queue(always the Head item/Node)
    if not self.is_empty():
      item_to_remove = self.head
      print('Removing {0} from the queue!'.format(str(item_to_remove.get_value())))
      if self.size == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
  
  def peek(self): #view the first item in the queue without removing from the queue
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self): #helper function to check the size of the queue
    return self.size
  
  def has_space(self): #helper function to check if queue has room
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self): #helper function to check if queue is empty
    return self.size == 0

q = Queue()
q.enqueue("some guy with a mustache") #Adding data "some guy with a mustache" to queue
q.dequeue() #removing data from queue