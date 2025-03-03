class StackNode:
    value: str
    next: "StackNode"

    def __init__(self, value, next=None):
        self.value = value    
        self.next = next


class StackList:
    top: StackNode

    def __init__(self, top):
        self.top = top


    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is None:
            return None
        self.top = self.top.next


    def print(self):
        curent = self.top
        while curent is not None:
            print(curent.value, end="\n")
            curent = curent.next
            

def main():
    # Create 3 nodes
    first_node = StackNode("first node")
    second_node = StackNode("second node", first_node)
    third_node = StackNode("third node", second_node)
    # Set up Stack
    stack = StackList(third_node)
    # Add node
    stack.push(StackNode("fourth node"))
    # Print Stack
    stack.print()
    # Deleting a node
    print(f"Delating top node with the value: {stack.top.value}")
    stack.pop()
    # Print updated Stack
    stack.print()

if __name__ == "__main__":
    main()