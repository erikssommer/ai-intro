from csp import *
import sys

level = sys.argv[1]
csp = create_sudoku_csp(f'{level}.txt')
print_sudoku_solution(csp.backtracking_search())
print(f"Backtrack method was called {csp.backtrack_count} times")
print(f"Backtrack method failed {csp.failure_count} times")
