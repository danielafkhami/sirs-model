import numpy as np

# SIRS Differential Equations
def sirs_system(y, beta, gamma, xi, N):
    S, I, R = y
    dSdt = -beta * S * I / N + xi * R
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I - xi * R

    return np.array([dSdt, dIdt, dRdt])

# RK4 Solver
def RungeKutta(y, dt, dydt, *args):
    k1 = dt * dydt(1.0 * y, *args)
    k2 = dt * dydt(1.0 * y + k1 * dt / 2, *args)
    k3 = dt * dydt(1.0 * y + k2 * dt / 2, *args)
    k4 = dt * dydt(1.0 * y + k3 * dt, *args)

    return y + (k1 + 2.0 * k2 + 2.0 * k3 + 1.0 * k4) / 6

def Euler(y, dt, dydt, *args):
    return y + dt * dydt(y, args)