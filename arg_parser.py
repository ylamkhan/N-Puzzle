# arg_parser.py
import argparse

def parse_arguments():
    """Parses command-line arguments for the N-puzzle solver."""
    parser = argparse.ArgumentParser(description="Solve the N-puzzle using A* search.")
    
    # Argument for file input or random generation
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str, help="Path to the puzzle file.")
    group.add_argument("-s", "--size", type=int, help="Size of a randomly generated puzzle (e.g., 3 for a 3x3 puzzle).")

    # Heuristic function choice
    parser.add_argument(
        "-H", "--heuristic",
        type=str,
        choices=['manhattan', 'misplaced', 'linear_conflict'],
        default='manhattan',
        help="Heuristic function to use. 'manhattan' is default."
    )
    
    # Search algorithm choice for bonus
    parser.add_argument(
        "-S", "--solver",
        type=str,
        choices=['astar', 'greedy', 'uniform'],
        default='astar',
        help="Search algorithm to use. 'astar' is default. 'greedy' and 'uniform' for bonus."
    )
    
    return parser.parse_args()