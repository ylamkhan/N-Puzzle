# puzzle_parser.py
import re

def parse_puzzle_file(filename):
    """
    Parses an N-puzzle file.
    
    Returns:
        tuple: A tuple of tuples representing the puzzle grid.
    """
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: File not found at '{filename}'")
        exit(1)

    # Filter out comments and empty lines
    clean_lines = []
    for line in lines:
        line = re.sub(r'#.*$', '', line).strip() # Remove comments
        if line:
            clean_lines.append(line)

    if not clean_lines:
        print("Error: Puzzle file is empty or contains only comments.")
        exit(1)

    try:
        size = int(clean_lines[0])
        grid_lines = clean_lines[1:]
        
        if len(grid_lines) != size:
            print(f"Error: Puzzle size is {size}, but {len(grid_lines)} rows were found.")
            exit(1)

        puzzle = []
        for line in grid_lines:
            row = [int(n) for n in line.split()]
            if len(row) != size:
                print(f"Error: Invalid row length. Expected {size} numbers.")
                exit(1)
            puzzle.append(tuple(row))
        
        return tuple(puzzle)

    except (ValueError, IndexError):
        print("Error: Invalid file format. Could not parse size or grid.")
        exit(1)