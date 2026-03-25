from sympy.ntheory.modular import solve_congruence
congruences = [(2, 5), (3, 11), (5, 17)]
solution = solve_congruence(*congruences)
print(solution)
