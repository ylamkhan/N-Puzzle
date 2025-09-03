# main.py
import sys
from arg_parser import parse_arguments
from puzzle_parser import parse_puzzle_file
from puzzle_generator import generate_solution, generate_random_puzzle
from solvability import is_solvable
from heuristics import manhattan_distance, misplaced_tiles, linear_conflict
from solver import solve

def print_puzzle(puzzle):
    """Prints the puzzle grid in a readable format."""
    size = len(puzzle)
    max_len = len(str(size * size - 1))
    for row in puzzle:
        print(" ".join(f"{num:>{max_len}}" for num in row))
    print()

def main():
    """Main function to run the N-puzzle solver."""
    args = parse_arguments()

    if args.file:
        puzzle = parse_puzzle_file(args.file)
        size = len(puzzle)
    else: # args.size
        size = args.size
        if size < 2:
            print("Error: Puzzle size must be at least 2.")
            exit(1)
        
        solution = generate_solution(size)
        puzzle = generate_random_puzzle(size)
        # Ensure the generated puzzle is solvable
        while not is_solvable(puzzle, solution):
            puzzle = generate_random_puzzle(size)
        print(f"Generated a solvable {size}x{size} puzzle:")
        print_puzzle(puzzle)
        
    solution = generate_solution(size)

    # Check for solvability
    if not is_solvable(puzzle, solution):
        print("This puzzle is unsolvable.")
        exit(0)

    # Select the heuristic function
    heuristic_map = {
        'manhattan': manhattan_distance,
        'misplaced': misplaced_tiles,
        'linear_conflict': linear_conflict
    }
    heuristic_func = heuristic_map[args.heuristic]
    
    print("Solving...")
    print(f"Algorithm: {args.solver.upper()}, Heuristic: {args.heuristic}")
    print("-" * 30)

    result = solve(puzzle, solution, heuristic_func, args.solver)

    if result is None:
        print("Could not find a solution.")
    else:
        print("Solution Found!")
        print(f"Total states selected (time complexity): {result['time_complexity']}")
        print(f"Max states in memory (size complexity): {result['size_complexity']}")
        print(f"Number of moves in solution: {result['moves']}")
        print("\nSolution Path:")
        for i, state in enumerate(result['path']):
            print(f"--- Move {i} ---")
            print_puzzle(state)

if __name__ == "__main__":
    main()