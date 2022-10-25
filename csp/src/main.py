from csp import *
import sys

level = sys.argv[1]
csp = create_sudoku_csp(f'{level}.txt')
print_sudoku_solution(csp.backtracking_search())
print(f"Number of times backtrack method was called: {csp.backtrack_count}")
print(f"Number of times backtrack method failed: {csp.failure_count}")
