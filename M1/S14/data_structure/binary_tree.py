class BinaryNode:
    data: int
    right_brach: "BinaryNode"
    left_brach: "BinaryNode"

    def __init__(self, data, right_brach=None, left_brach=None):
        self.data = data    
        self.right_brach = right_brach
        self.left_brach = left_brach

class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def insert_node(self, new_node):
        self._insert_recursive(self.root, new_node)

    def _insert_recursive(self,current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left_brach is None:
                current_node.left_brach = new_node
            else: 
                self._insert_recursive(current_node.left_brach, new_node)
        else:
            if current_node.right_brach is None:
                current_node.right_brach = new_node
            else:
                self._insert_recursive(current_node.right_brach, new_node)
            
    
    def print_tree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, current_node):
        if current_node is not None:  
            self._print_recursive(current_node.left_brach)  
            print(current_node.data, end=" ")  
            self._print_recursive(current_node.right_brach)  


def main():
    # Create binary tree
    tree = BinaryTree(BinaryNode(40))

    # Add nodes
    tree.insert_node(BinaryNode(10))
    tree.insert_node(BinaryNode(5))
    tree.insert_node(BinaryNode(15))
    tree.insert_node(BinaryNode(3))
    tree.insert_node(BinaryNode(7))
    tree.insert_node(BinaryNode(12))
    tree.insert_node(BinaryNode(18))

    # Print tree
    print("Árbol binario (in-order traversal):")
    tree.print_tree()


if __name__=='__main__':
    main()