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
    k1 = dt * dydt(y, *args)
    k2 = dt * dydt(y + k1 * dt / 2., *args)
    k3 = dt * dydt(y + k2 * dt / 2., *args)
    k4 = dt * dydt(y + k3 * dt, *args)

    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.