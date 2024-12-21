from collections import defaultdict

def dfs(graph, start, goal):
    visited = []  # List for visited nodes
    stack = [start]  # Initialize a stack with the start node
    parent = {start: None}  # Dictionary to store parent nodes

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            if node == goal:
                return visited, reconstruct_path(parent, start, goal)

            # Add all unvisited neighbors to the stack
            for neighbour in graph.get(node, []):
                if neighbour not in visited:  # Check if neighbour has not been visited
                    parent[neighbour] = node
                    stack.append(neighbour)

    return visited, None  # Return visited nodes and None if there is no path

def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()  # Reverse the path to start from the source
    return path

def print_dfs_with_path(graph, start, goal):
    visited, path = dfs(graph, start, goal)
    print("Order of nodes visited:", " -> ".join(visited))
    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")

def main():
    graphs = {
        '1': {
            'a': [],
            'b': ['a'],
            'c': ['a'],
            'd': ['b', 'c', 'e'],
            'e': ['h', 'r'],
            'f': ['c', 'g'],
            'g': [],
            'h': ['p', 'q'],
            'p': ['q'],
            'q': [],
            'r': ['f'],
            's': ['d', 'e', 'p']
        },
        '2': {
            'a': ['b', 'c'],
            'b': ['a', 'd'],
            'c': ['a', 'k'],
            'd': ['b', 'e', 'm'],
            'e': ['d', 'n'],
            'f': ['p', 's'],
            'g': ['m', 't'],
            'h': ['k', 's'],
            'k': ['c', 'h'],
            'm': ['d', 'g', 'n'],
            'n': ['e', 'm'],
            'p': ['f', 'q'],
            'q': ['p', 'r'],
            'r': ['q', 't'],
            's': ['f', 'h'],
            't': ['g', 'r']
        },
        '3': {
            'a': ['b', 'c'],
            'b': ['a', 'c', 'd'],
            'c': ['a', 'b', 'd'],
            'd': ['b', 'c', 'e', 'f', 'g'],
            'e': ['d', 'g'],
            'f': ['d', 'g'],
            'g': ['d', 'e', 'f']
        }
    }

    # Input handling
    graph_type = input("Enter graph type (1, 2, 3): ")
    if graph_type not in graphs:
        print("Invalid graph type.")
        return

    graph = graphs[graph_type]
    start_node = input("Enter start node: ")
    end_node = input("Enter end node: ")

    print_dfs_with_path(graph, start_node, end_node)

# Run the main function
if __name__ == "__main__":
    main()
