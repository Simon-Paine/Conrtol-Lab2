import sympy as sym

# Step 0 - introduce the necessary symbols
M, m, g, x1, x2, x3, x4, F, ell = sym.symbols('M, m, g, x1 , x2 , x3 , x4 , F, ell')
phi = 4 * m * ell * x4**2 * sym.sin(x3) + 4*F - 3*m*g*sym.sin(x3)*sym.cos(x3)
phi /= 4*(M+m) - 3*m*sym.cos(x3)**2


# Step 1 - Differentiate phi wrt F, x3, x4
d_phi_F = phi.diff(F)
d_phi_x3 = phi.diff(x3)
d_phi_x4 = phi.diff(x4)


def evaluate_at_equilibrium(f):
    """
    This function evaluates the equation
    at the F=0, x3=0 and x4=0
    """
    return f.subs([(F, 0), (x3, 0), (x4, 0)])


# Step 2 - sub F=0, x3=0, x4=0 into above derivatives
d_phi_F_eq = evaluate_at_equilibrium(d_phi_F)
d_phi_x3_eq = evaluate_at_equilibrium(d_phi_x3)
d_phi_x4_eq = evaluate_at_equilibrium(d_phi_x4)

# Printing psi at equilibrium point
print('Phi evaluated at F:')
sym.pprint(d_phi_F_eq)
print()
print('Phi evaluated at x3:')
sym.pprint(d_phi_x3_eq)
print()
print('Phi evaluated at x4:')
sym.pprint(d_phi_x4_eq)
