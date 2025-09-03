# puzzle_generator.py
import random

def generate_solution(size):
    """Generates the target 'snail' solution grid for a given size."""
    grid = [[0] * size for _ in range(size)]
    x, y = 0, 0
    dx, dy = 1, 0
    num = 1
    
    for i in range(size * size - 1):
        grid[y][x] = num
        num += 1
        
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx # Turn right
            x, y = x + dx, y + dy
            
    return tuple(tuple(row) for row in grid)

def generate_random_puzzle(size):
    """Generates a random, shuffled puzzle of a given size."""
    numbers = list(range(size * size))
    random.shuffle(numbers)
    
    puzzle = []
    for i in range(size):
        row = tuple(numbers[i * size : (i + 1) * size])
        puzzle.append(row)
        
    return tuple(puzzle)