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
    
    def dfs_lowest_cost_path(self, node, end, path=None, cost=0, best=None):
        if path is None:
            path = []
        
        node.visited = True
        path.append(node.value)
        
        if node.value == end:
            if best is None or cost < best[1]:
                best = (path[:], cost)
        else:
            adj = node.next_adjacent
            while adj:
                next_node = self.find_vertice(adj.value)
                if next_node and not next_node.visited:
                    best = self.dfs_lowest_cost_path(next_node, end, path, cost + adj.adjacent_weight, best)
                adj = adj.next_adjacent
        
        node.visited = False
        path.pop()
        return best
    
    def find_lowest_cost_path(self, start, end):
        start_node = self.find_vertice(start)
        if not start_node:
            return None
        
        result = self.dfs_lowest_cost_path(start_node, end)
        return result

    

grafo = LinkedList()
cidades = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
for cidade in cidades:
    grafo.insert_next_vertice(cidade)

grafo.insert_edge("A", "B", 10)
grafo.insert_edge("A", "C", 5)
grafo.insert_edge("A", "D", 1)
grafo.insert_edge("B", "C", 3)
grafo.insert_edge("B", "E", 10)
grafo.insert_edge("C", "F", 10)
grafo.insert_edge("D", "E", 2)
grafo.insert_edge("D", "G", 2)
grafo.insert_edge("E", "F", 1)
grafo.insert_edge("E", "H", 10)
grafo.insert_edge("F", "I", 10)
grafo.insert_edge("G", "H", 3)
grafo.insert_edge("H", "I", 1)
grafo.insert_edge("I", "J", 10)
grafo.insert_edge("J", "K", 10)
grafo.insert_edge("K", "L", 10)
grafo.insert_edge("L", "M", 10)
grafo.insert_edge("D", "M", 1)


melhor_caminho, menor_custo = grafo.find_lowest_cost_path("A", "M")
print(f"Melhor caminho: {melhor_caminho}, Menor custo: {menor_custo}")
