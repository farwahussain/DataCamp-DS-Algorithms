#implement a function to insert a node into a Binary Search Tree

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left_child = left
        self.right_child = right
      

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = TreeNode(data)
    # Check if the BST is empty
    if self.root == None:
      self.root = new_node
      return
    else:
      current_node = self.root
      while True:
        # Check if the data to insert is smaller than the current node's data
        if data < current_node.data:
          if current_node.left_child == None:
            current_node.left_child = new_node
            return 
          else:
            current_node = current_node.left_child
        # Check if the data to insert is greater than the current node's data
        elif data > current_node.data:
          if current_node.right_child == None:
            current_node.right_child = new_node
            return
          else:
            current_node = current_node.right_child

def CreateTree():
    bst = BinarySearchTree()
    # Insert nodes according to the provided tree structure
    bst.insert("Little Women")
    bst.insert("Heidi")
    bst.insert("Oliver Twist")
    bst.insert("Dracula")
    bst.insert("Jane Eyre")
    bst.insert("Moby Dick")
    bst.insert("Vanity Fair")
    return bst

def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
                
        return False
    

bst = CreateTree()
bst.insert("Pride and Prejudice")
print(search(bst, "Pride and Prejudice"))