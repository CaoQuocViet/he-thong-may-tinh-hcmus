import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from heuristics import heuristics
from graphs import graphs

def a_star_algorithm(adjacency_list, heuristic, start_node, stop_node):
    open_list = {start_node}
    closed_list = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    nodes_visited = 0

    while open_list:
        n = min(open_list, key=lambda v: g[v] + heuristic[v])

        if n == stop_node:
            reconst_path = []
            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]
            reconst_path.append(start_node)
            reconst_path.reverse()
            print(f'    Path found: {reconst_path}')
            print(f'    Nodes visited: {nodes_visited + 1}') 
            return reconst_path

        open_list.remove(n)
        closed_list.add(n)
        nodes_visited += 1

        for m, weight in adjacency_list[n]:
            if m not in closed_list:
                if m not in open_list or g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    open_list.add(m)

    print('Path does not exist!')
    print(f'Nodes visited: {nodes_visited}')
    return None


def ucs_algorithm(adjacency_list, start_node, stop_node):
    open_list = {start_node}
    closed_list = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    nodes_visited = 0

    while open_list:
        n = min(open_list, key=lambda v: g[v])

        if n == stop_node:
            reconst_path = []
            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]
            reconst_path.append(start_node)
            reconst_path.reverse()
            print(f'    Path found: {reconst_path}')
            print(f'    Nodes visited: {nodes_visited + 1}') 
            return reconst_path

        open_list.remove(n)
        closed_list.add(n)
        nodes_visited += 1

        for m, weight in adjacency_list[n]:
            if m not in closed_list:
                if m not in open_list or g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    open_list.add(m)

    print('Path does not exist!')
    print(f'Nodes visited: {nodes_visited}')
    return None


def greedy_algorithm(adjacency_list, heuristic, start_node, stop_node):
    open_list = {start_node}
    closed_list = set()
    parents = {start_node: start_node}
    nodes_visited = 0

    while open_list:
        n = min(open_list, key=lambda v: heuristic[v])

        if n == stop_node:
            reconst_path = []
            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]
            reconst_path.append(start_node)
            reconst_path.reverse()
            print(f'    Path found: {reconst_path}')
            print(f'    Nodes visited: {nodes_visited + 1}') 
            return reconst_path

        open_list.remove(n)
        closed_list.add(n)
        nodes_visited += 1

        for m, _ in adjacency_list[n]:
            if m not in closed_list:
                if m not in open_list:
                    open_list.add(m)
                    parents[m] = n

    print('Path does not exist!')
    print(f'Nodes visited: {nodes_visited}')
    return None


# Example usage:
if __name__ == "__main__":
    # A* algorithm
    print('A* algorithm:')
    a_star_algorithm(graphs['1'], heuristics['1'], 'S', 'G')
    a_star_algorithm(graphs['2'], heuristics['2'], 's', 'g')
    a_star_algorithm(graphs['3'], heuristics['3.1'], 'A', 'G')
    a_star_algorithm(graphs['3'], heuristics['3.2'], 'A', 'G')
    a_star_algorithm(graphs['4'], heuristics['4'], 'Arad', 'Bucharest')

    # UCS algorithm
    print()
    print('UCS algorithm:')
    ucs_algorithm(graphs['1'], 'S', 'G')
    ucs_algorithm(graphs['2'], 's', 'g')
    ucs_algorithm(graphs['3'], 'A', 'G')
    ucs_algorithm(graphs['4'], 'Arad', 'Bucharest')

    # Greedy algorithm
    print()
    print('Greedy algorithm:')
    greedy_algorithm(graphs['1'], heuristics['1'], 'S', 'G')
    greedy_algorithm(graphs['2'], heuristics['2'], 's', 'g')
    greedy_algorithm(graphs['3'], heuristics['3.1'], 'A', 'G')
    greedy_algorithm(graphs['3'], heuristics['3.2'], 'A', 'G')
    greedy_algorithm(graphs['4'], heuristics['4'], 'Arad', 'Bucharest')
