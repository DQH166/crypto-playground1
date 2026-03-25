from sympy import mod_inverse,sqrt_mod

file_path = 'output_MSR.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

a_cleaned = lines[0].split('=')[1].strip()
p_cleaned = lines[1].split('=')[1].strip()

a = int(a_cleaned)
p = int(p_cleaned)

print(a)
print(p)

sqrt_a_mod_p = sqrt_mod(a, p, all_roots=True)
sqrt_a_mid_p_min = min(sqrt_a_mod_p)

print(sqrt_a_mid_p_min)
