import sympy as sym

# Step 0 - introduce the necessary symbols
M, m, g, x1, x2, x3, x4, F, ell = sym.symbols('M, m, g, x1 , x2 , x3 , x4 , F, ell')
psi = -3*(m*ell*x4**2*sym.sin(x3) + F*sym.cos(x3) - (M+m)*g*sym.sin(x3))
psi /= (4*(M+m) - 3*m*sym.cos(x3)**2)*ell


# Step 1 - Differentiate psi wrt F, x3, x4
d_psi_F = psi.diff(F)
d_psi_x3 = psi.diff(x3)
d_psi_x4 = psi.diff(x4)


def evaluate_at_equilibrium(f):
    """
    This function evaluates the equation
    at the F=0, x3=0 and x4=0
    """
    return f.subs([(F, 0), (x3, 0), (x4, 0)])


# Step 2 - sub F=0, x3=0, x4=0 into above derivatives
d_psi_F_eq = evaluate_at_equilibrium(d_psi_F)
d_psi_x3_eq = evaluate_at_equilibrium(d_psi_x3)
d_psi_x4_eq = evaluate_at_equilibrium(d_psi_x4)

# Printing psi at equilibrium point
print('Psi evaluated at F:')
sym.pprint(d_psi_F_eq)
print()
print('Psi evaluated at x3:')
sym.pprint(d_psi_x3_eq)
print()
print('Psi evaluated at x4:')
sym.pprint(d_psi_x4_eq)
