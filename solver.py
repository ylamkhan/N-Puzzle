# solver.py
import heapq
import time
from heuristics import get_solution_map

class Node:
    """A node in the search tree."""
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost from current node to goal

    @property
    def f(self):
        """Total estimated cost."""
        return self.g + self.h

    def __lt__(self, other):
        """Comparison for priority queue."""
        return self.f < other.f

    def __eq__(self, other):
        """Equality check."""
        return self.state == other.state

    def __hash__(self):
        """Hash for storing in sets."""
        return hash(self.state)

def get_neighbors(state):
    """Generates all possible neighbor states from the current state."""
    size = len(state)
    neighbors = []
    
    # Find the position of the empty tile (0)
    zero_pos = None
    for r in range(size):
        for c in range(size):
            if state[r][c] == 0:
                zero_pos = (r, c)
                break
        if zero_pos:
            break
            
    r, c = zero_pos
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < size and 0 <= nc < size:
            new_state_list = [list(row) for row in state]
            new_state_list[r][c], new_state_list[nr][nc] = new_state_list[nr][nc], new_state_list[r][c]
            neighbors.append(tuple(tuple(row) for row in new_state_list))
            
    return neighbors

def reconstruct_path(node):
    """Reconstructs the solution path from the goal node."""
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1] # Reverse to get path from start to goal

def solve(puzzle, solution, heuristic_func, solver_type):
    """
    Solves the N-puzzle using the specified search algorithm and heuristic.
    
    Returns:
        A dictionary containing the solution details.
    """
    solution_map = get_solution_map(solution)
    
    start_h = heuristic_func(puzzle, solution_map)
    start_g = 0
    
    # Adjust g and h based on solver type (for bonus)
    if solver_type == 'greedy':
        start_g = 0
    if solver_type == 'uniform':
        start_h = 0
        
    start_node = Node(state=puzzle, parent=None, g=start_g, h=start_h)

    open_set = [start_node] # Priority queue
    closed_set = set()
    open_map = {start_node.state: start_node} # For efficient lookups

    time_complexity = 0
    size_complexity = 1

    while open_set:
        current_node = heapq.heappop(open_set)
        del open_map[current_node.state]

        if current_node.state == solution:
            path = reconstruct_path(current_node)
            return {
                "path": path,
                "moves": len(path) - 1,
                "time_complexity": time_complexity,
                "size_complexity": size_complexity
            }

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue

            g_cost = current_node.g + 1
            h_cost = heuristic_func(neighbor_state, solution_map)
            
            # Adjust costs for bonus solvers
            if solver_type == 'greedy':
                g_cost = 0
            if solver_type == 'uniform':
                h_cost = 0

            neighbor_node = Node(state=neighbor_state, parent=current_node, g=g_cost, h=h_cost)
            
            if neighbor_state not in open_map or neighbor_node.g < open_map[neighbor_state].g:
                heapq.heappush(open_set, neighbor_node)
                open_map[neighbor_state] = neighbor_node
                time_complexity += 1

        size_complexity = max(size_complexity, len(open_set) + len(closed_set))

    return None # No solution found