class DoubleQueueNode:
    data: str
    next: "DoubleQueueNode"
    previous: "DoubleQueueNode"

    def __init__(self, data, next=None, previous=None):
        self.data = data    
        self.next = next
        self.previous = previous 


class DoubleQueueList:
    head: DoubleQueueNode
    tail: DoubleQueueNode


    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


    def push_right(self, new_node):
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node


    def push_left(self, new_node):
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def pop_right (self):
        if self.tail is None:  # If head is void
            return None
        if self.head == self.tail: # If there is only a node
            self.head = None
            self.tail = None
        else: # Delete last node 
            self.tail = self.tail.previous
            self.tail.next = None
    

    def pop_left (self):
        if self.head is None:  # If head is void
            return None
        if self.head == self.tail: # If there is only a node
            self.head = None
            self.tail = None
        else: # Delete first node 
            self.head = self.head.next
            self.head.previous = None


    def print(self):
        curent = self.head
        while curent is not None:
            print(curent.data, end=" ")
            curent = curent.next
            


def main():
    # Create 3 nodes
    last_node = DoubleQueueNode("last_node")
    first_node = DoubleQueueNode("first_node", next=last_node)
    # Set up Double Ended Queue
    double_queue = DoubleQueueList(first_node, last_node)
    # Print Double Ended Queue
    print("----Nodes----")
    double_queue.print()
    # Add right
    print("\n--Add-right--")
    double_queue.push_right(DoubleQueueNode("new_last_node"))
    double_queue.print()
    # Add left
    print("\n--Add--left--")
    double_queue.push_left(DoubleQueueNode("new_first_node"))
    double_queue.print()
    # Remove right
    print("\n--rm--right--")
    double_queue.pop_right()
    double_queue.print()
    # Remove left
    print("\n--rm--left--")
    double_queue.pop_left()
    double_queue.print()

if __name__ == "__main__":
    main()