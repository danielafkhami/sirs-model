import numpy as np

# SIRS Differential Equations
def sirs_system(y, beta, gamma, xi, birth, death):
    S, I, R = y
    N = S + I + R
    dSdt = -beta * S * I / N + xi * R + birth - death * S / N
    dIdt = beta * S * I / N - gamma * I - death * I / N
    dRdt = gamma * I - xi * R - death * R / N

    return np.array([dSdt, dIdt, dRdt])

# RK4 Solver
def RungeKutta(y, dt, dydt, *args):
    k1 = dt * dydt(1.0 * y, *args)
    k2 = dt * dydt(1.0 * y + k1 * dt / 2, *args)
    k3 = dt * dydt(1.0 * y + k2 * dt / 2, *args)
    k4 = dt * dydt(1.0 * y + k3 * dt, *args)

    return y + (k1 + 2.0 * k2 + 2.0 * k3 + 1.0 * k4) / 6