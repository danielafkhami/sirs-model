import matplotlib.pyplot as plt
from params import *
from model import *

steps = int(T / dt)

valuesSIRS = np.zeros((steps, 3))
valuesSIR = np.zeros((steps, 3))
valuesSIRS[0] = [S0, I0, R0]
valuesSIR[0] = [S0, I0, R0]

t_axis = np.linspace(0, T, steps)

# Simulation
for i in range(1, steps):
    valuesSIRS[i] = RungeKutta(valuesSIRS[i-1], dt, sirs_system, beta, gamma, xi, N)
    valuesSIR[i] = RungeKutta(valuesSIR[i-1], dt, sirs_system, beta, gamma, 0, N)

def plot(values, method):
    plt.figure(figsize=(10, 6))
    plt.plot(t_axis, values[:, 0], label='Susceptible', color='blue')
    plt.plot(t_axis, values[:, 1], label='Infected', color='red')
    plt.plot(t_axis, values[:, 2], label='Recovered', color='green')

    plt.title(f"{method}\n$\\beta={beta}, \\gamma={gamma}, \\xi={xi}$")
    plt.xlabel("Time (Days)")
    plt.ylabel("Population")
    plt.grid(alpha=0.3)
    plt.legend()

plot(valuesSIRS, "SIRS Model Simulation : Runge-Kutta")
plot(valuesSIR, "SIR Model Simulation : Runge-Kutta")
plt.show()

print(f'\nSusceptible RK: {round(valuesSIRS[-1, 0], 2)}')
print(f'Infected ~ 0 RK: {valuesSIRS[-1, 1] < 1}')
print(f'Recovered RK: {round(valuesSIRS[-1, 2], 2)}\n')
print(f'\nSusceptible E: {round(valuesSIR[-1, 0], 2)}')