class Node:
    def __init__(self, value, weight=None):
        self.value = value
        self.next_adjacent = None
        self.adjacent_weight = weight
        self.next_vertice = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_next_adjacent(self, value, vertice_head, weight=None):
        current_node = self.head

        while current_node.value != vertice_head:
            current_node = current_node.next_vertice

        new_node = Node(value, weight)

        if current_node.next_adjacent is None:
            current_node.next_adjacent = new_node
        else:
            while(current_node.next_adjacent):
                current_node = current_node.next_adjacent
            current_node.next_adjacent = new_node

    def insert_next_vertice(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head 

        while(current_node.next_vertice):
            current_node = current_node.next_vertice
        current_node.next_vertice = new_node

    def print_list(self):
        current_node = self.head

        while current_node:
            print(f"{current_node.value} ->", end=" ")
            adj = current_node.next_adjacent
            while adj:
                print(
                    f"{adj.value}" + (f"({adj.adjacent_weight})" if adj.adjacent_weight else ""), 
                    end=" -> " if adj.next_adjacent else "\n"
                )
                adj = adj.next_adjacent
            current_node = current_node.next_vertice

vertices = LinkedList()
vertices.insert_next_vertice(1)
vertices.insert_next_vertice(2)
vertices.insert_next_vertice(3)
vertices.insert_next_adjacent(2, 1)
vertices.insert_next_adjacent(3, 1)
vertices.insert_next_adjacent(4, 1)
vertices.insert_next_adjacent(1, 2)
vertices.insert_next_adjacent(3, 2, 5)
vertices.insert_next_adjacent(4, 2)
vertices.insert_next_adjacent(5, 2)
vertices.insert_next_adjacent(1, 3)
vertices.insert_next_adjacent(2, 3)
vertices.insert_next_adjacent(5, 3)
vertices.print_list()

