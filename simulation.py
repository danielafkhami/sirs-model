import matplotlib.pyplot as plt
from params import *
from model import *

steps = int(T / dt)

values_SIRS_VD = np.zeros((steps, 3))
values_SIR_VD = np.zeros((steps, 3))
values_SIRS = np.zeros((steps, 3))
values_SIR = np.zeros((steps, 3))
values_SIRS_VD[0] = [S0, I0, R0]
values_SIR_VD[0] = [S0, I0, R0]
values_SIRS[0] = [S0, I0, R0]
values_SIR[0] = [S0, I0, R0]
t_axis = np.linspace(0, T, steps)

# Simulation
for i in range(1, steps):
    values_SIRS_VD[i] = RungeKutta(values_SIRS_VD[i-1], dt, sirs_system, beta, gamma, xi, lambd, mu)
    values_SIR_VD[i] = RungeKutta(values_SIR_VD[i-1], dt, sirs_system, beta, gamma, 0, lambd, mu)
    values_SIRS[i] = RungeKutta(values_SIRS[i-1], dt, sirs_system, beta, gamma, xi, 0, 0)
    values_SIR[i] = RungeKutta(values_SIR[i-1], dt, sirs_system, beta, gamma, 0, 0, 0)

def plot(values, name, sirs, vd):
    plt.figure(figsize=(10, 6))
    plt.plot(t_axis, values[:, 0], label='Susceptible', color='blue')
    plt.plot(t_axis, values[:, 1], label='Infected', color='red')
    plt.plot(t_axis, values[:, 2], label='Recovered', color='green')
    if (vd):
        plt.plot(t_axis, values[:, 0] + values[:, 1] + values[:, 2], label='Population', color='black')

    title = f"{name}\n$\\beta={beta}, \\gamma={gamma}$"
    if (sirs and vd):
        title = f"{name}\n$\\beta={beta}, \\gamma={gamma}, \\xi={xi}, \\lambda={lambd}, \\mu={mu}$"
    elif (sirs):
        title = f"{name}\n$\\beta={beta}, \\gamma={gamma}, \\xi={xi}$"
    elif (vd):
        title = f"{name}\n$\\beta={beta}, \\gamma={gamma}, \\lambda={lambd}, \\mu={mu}$"

    plt.title(title)
    plt.xlabel("Time (Days)")
    plt.ylabel("Population")
    plt.grid(alpha=0.3)
    plt.legend()

plot(values_SIRS_VD, "SIRS Vital Dynamics Model Simulation : Runge-Kutta", True, True)
plot(values_SIR_VD, "SIR Vital Dynamics Model Simulation : Runge-Kutta", False, True)
plot(values_SIRS, "SIRS Model Simulation : Runge-Kutta", True, False)
plot(values_SIR, "SIR Model Simulation : Runge-Kutta", False, False)
plt.show()