# Makefile for the N-Puzzle project

# Define the Python interpreter
PYTHON = python3

# Define the main script
MAIN_SCRIPT = main.py

# Default rule: runs a simple 3x3 puzzle from a file
all: run_file

# Rule to run the solver with a specific file
# Example: make run_file FILE=puzzles/3x3.txt HEURISTIC=manhattan
run_file:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make run_file FILE=<path_to_puzzle>"; \
		exit 1; \
	fi
	$(PYTHON) $(MAIN_SCRIPT) -f $(FILE) -H $(or $(HEURISTIC),manhattan) -S $(or $(SOLVER),astar)

# Rule to run the solver with a randomly generated puzzle of a given size
# Example: make run_random SIZE=3 HEURISTIC=misplaced SOLVER=greedy
run_random:
	@if [ -z "$(SIZE)" ]; then \
		echo "Usage: make run_random SIZE=<puzzle_size>"; \
		exit 1; \
	fi
	$(PYTHON) $(MAIN_SCRIPT) -s $(SIZE) -H $(or $(HEURISTIC),manhattan) -S $(or $(SOLVER),astar)

# Clean up Python cache files
clean:
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@echo "Cleaned up Python cache files."

.PHONY: all run_file run_random clean