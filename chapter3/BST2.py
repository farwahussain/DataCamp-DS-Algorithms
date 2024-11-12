#find the minimum node

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


  def find_min(self):
    # Set current_node as the root
    current_node = self.root
    # Iterate over the nodes of the appropriate subtree
    while current_node.left_child:
      # Update current_node
      current_node = current_node.left_child
    return current_node.data
  
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

bst = CreateTree()
print(bst.find_min())