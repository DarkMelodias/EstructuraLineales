from node import Node

class CircleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, data):
        """Insert a new Node

        data: is of value for Node
        """
        node = Node(data)

        if self.head == None:
            self.head = node
            self.head.next = self.head
        else:
            node.next = self.head
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = node

        self.size += 1

    def print(self):
        """Print all value of nodes
        """
        current = self.head
        node_numbers = self.size
        while node_numbers > 0:
            print(f'The Node {current} have value {current.data}')
            current = current.next
            node_numbers -= 1

def main():
    node_numbers = int(input('Insert numbers of Nodes: '))
    node = CircleLinkedList()
    total_nodes = node_numbers
    while node_numbers > 0:
        data_node = str(input(f'¿What is the value of node number {total_nodes - (node_numbers - 1)}?: '))
        node.append(data_node)
        node_numbers -= 1

    probe = node
    print(probe.head.next.data)

if __name__ == '__main__':
    main()