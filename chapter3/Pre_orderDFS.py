class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def pre_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Print the value of the current_node
            print(current_node.data, end=' ')
            # Call pre_order recursively on the left and right children
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)
    
    def create_expression_tree(self):
        # Create nodes for each part of the expression
        multiply = Node('*')
        subtract = Node('-')
        num10 = Node(10)
        num5 = Node(5)
        num3 = Node(3)

        # Build the tree structure
        multiply.left_child = subtract
        multiply.right_child = num3
        subtract.left_child = num10
        subtract.right_child = num5

        # Set the root of the tree
        self.root = multiply

# Create an instance of ExpressionTree
et = ExpressionTree()
et.create_expression_tree()  # Initialize the tree for the expression (10 - 5) * 3
et.pre_order(et.root)  # Perform pre-order traversal
