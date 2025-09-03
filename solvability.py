# solvability.py

def count_inversions(flat_puzzle):
    """Counts the number of inversions in a flattened puzzle."""
    inversions = 0
    size = len(flat_puzzle)
    for i in range(size):
        for j in range(i + 1, size):
            # Ignore the empty tile (0)
            if flat_puzzle[i] != 0 and flat_puzzle[j] != 0 and flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions

def find_zero_row_from_bottom(puzzle):
    """Finds the row of the empty tile (0), counting from the bottom (1-indexed)."""
    size = len(puzzle)
    for r in range(size):
        for c in range(size):
            if puzzle[r][c] == 0:
                return size - r
    return -1 # Should not happen

def is_solvable(puzzle, solution):
    """
    Checks if an N-puzzle is solvable based on the number of inversions.
    See: https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
    """
    size = len(puzzle)
    flat_puzzle = [num for row in puzzle for num in row]
    inversions = count_inversions(flat_puzzle)

    if size % 2 != 0: # Odd-sized grid
        return inversions % 2 == 0
    else: # Even-sized grid
        zero_row = find_zero_row_from_bottom(puzzle)
        if zero_row % 2 != 0: # Zero is on an odd row from bottom
            return inversions % 2 == 0
        else: # Zero is on an even row from bottom
            return inversions % 2 != 0