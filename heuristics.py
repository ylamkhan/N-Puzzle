# heuristics.py

def get_solution_map(solution):
    """Creates a map of value -> (row, col) for the solution state."""
    size = len(solution)
    solution_map = {}
    for r in range(size):
        for c in range(size):
            solution_map[solution[r][c]] = (r, c)
    return solution_map

def manhattan_distance(puzzle, solution_map):
    """Calculates the Manhattan distance heuristic."""
    distance = 0
    size = len(puzzle)
    for r in range(size):
        for c in range(size):
            value = puzzle[r][c]
            if value != 0:
                goal_r, goal_c = solution_map[value]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def misplaced_tiles(puzzle, solution_map):
    """Calculates the misplaced tiles heuristic."""
    misplaced = 0
    size = len(puzzle)
    for r in range(size):
        for c in range(size):
            value = puzzle[r][c]
            if value != 0:
                goal_r, goal_c = solution_map[value]
                if r != goal_r or c != goal_c:
                    misplaced += 1
    return misplaced

def linear_conflict(puzzle, solution_map):
    """Calculates the Manhattan distance + Linear Conflict heuristic."""
    size = len(puzzle)
    manhattan = manhattan_distance(puzzle, solution_map)
    conflicts = 0

    # Row conflicts
    for r in range(size):
        for c1 in range(size):
            tile1 = puzzle[r][c1]
            if tile1 == 0: continue
            goal_r1, _ = solution_map[tile1]
            if r != goal_r1: continue
            
            for c2 in range(c1 + 1, size):
                tile2 = puzzle[r][c2]
                if tile2 == 0: continue
                goal_r2, _ = solution_map[tile2]
                if r != goal_r2: continue
                
                # If tile1 and tile2 are in their goal row but in the wrong order
                if solution_map[tile1][1] > solution_map[tile2][1]:
                    conflicts += 2

    # Column conflicts
    for c in range(size):
        for r1 in range(size):
            tile1 = puzzle[r1][c]
            if tile1 == 0: continue
            _, goal_c1 = solution_map[tile1]
            if c != goal_c1: continue

            for r2 in range(r1 + 1, size):
                tile2 = puzzle[r2][c]
                if tile2 == 0: continue
                _, goal_c2 = solution_map[tile2]
                if c != goal_c2: continue

                if solution_map[tile1][0] > solution_map[tile2][0]:
                    conflicts += 2
    
    return manhattan + conflicts