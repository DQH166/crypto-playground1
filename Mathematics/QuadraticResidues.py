def is_quadratic_residue(x, p):
    for a in range(1,p):
        if (a*a) % p == x:
            return True
    return False

p = 29
ints = [14,6,11]

quadratic_residues = []
for x in ints:
    if is_quadratic_residue(x,p):
        quadratic_residues.append(x)

print(quadratic_residues)


def find_square_root(x,p):
    for a in range(1,p):
        if (a*a)%p == x:
            return a
    return None

square_root_of_6 = find_square_root(6,p)

print(square_root_of_6)
