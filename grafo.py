class Node:
    def __init__(self, value, weight=None):
        self.value = value
        self.next_adjacent = None
        self.adjacent_weight = weight
        self.visited = False
        self.next_vertice = None
class Queue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        return self.elements.pop(0)

class LinkedList:
    def __init__(self):
        self.head = None

    def find_vertice(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next_vertice
        return None

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

    def insert_edge(self, from_value, to_value, weight):
        from_node = self.find_vertice(from_value)
        to_node = self.find_vertice(to_value)

        if from_node and to_node:
            new_adj = Node(to_value)  # destination value
            new_adj.adjacent_weight = weight  # Store weight
            new_adj.next_adjacent = from_node.next_adjacent 
            from_node.next_adjacent = new_adj

    def dfs_highest_cost_path(self, node, path=None, cost=0):
        node.visited = True
        path.append(node.value)
        best_path, max_cost = path[:], cost

        adj = node.next_adjacent
        while adj:
            next_node = self.find_vertice(adj.value)
            if next_node and not next_node.visited:
                new_path, new_cost = self.dfs_highest_cost_path(next_node, path[:], cost + adj.adjacent_weight)
                if new_cost > max_cost:
                    best_path, max_cost = new_path, new_cost
            adj = adj.next_adjacent

        node.visited = False  # Allow revisiting
        return best_path, max_cost


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

    def bfs_shortest_path(self, start: str, end: str):
        if not self.head:
            return None

        queue = [(start, [start])]  # (current node, path so far)

        while queue:
            current, path = queue.pop(0)

            node = self.head
            while node and node.value != current:
                node = node.next_vertice

            if node and not node.visited:
                node.visited = True

                if node.value == end:
                    return path

                adj = node.next_adjacent
                while adj:
                    if not adj.visited:
                        queue.append((adj.value, path + [adj.value]))
                    adj = adj.next_adjacent

        return None
    

graph = LinkedList()

for city in ["A", "B", "C", "D", "E", "F"]:
    graph.insert_next_vertice(city)

graph.insert_next_adjacent("B", "A")
graph.insert_next_adjacent("C", "A")
graph.insert_next_adjacent("D", "B")
graph.insert_next_adjacent("E", "B")
graph.insert_next_adjacent("F", "C")
graph.insert_next_adjacent("E", "D")
graph.insert_next_adjacent("F", "E")

print(graph.bfs_shortest_path("A", "F"))  # ['A', 'C', 'F']

# vertices = LinkedList()
# vertices.insert_next_vertice(1)
# vertices.insert_next_vertice(2)
# vertices.insert_next_vertice(3)
# vertices.insert_next_adjacent(2, 1)
# vertices.insert_next_adjacent(3, 1)
# vertices.insert_next_adjacent(4, 1)
# vertices.insert_next_adjacent(1, 2)
# vertices.insert_next_adjacent(3, 2, 5)
# vertices.insert_next_adjacent(4, 2)
# vertices.insert_next_adjacent(5, 2)
# vertices.insert_next_adjacent(1, 3)
# vertices.insert_next_adjacent(2, 3)
# vertices.insert_next_adjacent(5, 3)
# vertices.print_list()

