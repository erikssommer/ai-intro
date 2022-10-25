from csp import *
import sys

level = sys.argv[1]
csp = create_sudoku_csp(f'{level}.txt')
print_sudoku_solution(csp.backtracking_search())
