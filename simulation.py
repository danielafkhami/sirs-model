import matplotlib.pyplot as plt
from params import *
from model import *

steps = int(T / dt)
values = np.zeros((steps, 3))
t_axis = np.linspace(0, T, steps)
values[0] = [S0, I0, R0]

# Simulation
for i in range(1, steps):
    values[i] = RungeKutta(values[i-1], dt, sirs_system, beta, gamma, xi, N)

def plot():
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t_axis, values[:, 0], label='Susceptible', color='blue')
    plt.plot(t_axis, values[:, 1], label='Infected', color='red')
    plt.plot(t_axis, values[:, 2], label='Recovered', color='green')

    plt.title(f"SIRS Model Simulation\n$\\beta={beta}, \\gamma={gamma}, \\xi={xi}$")
    plt.xlabel("Time (Days)")
    plt.ylabel("Population")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

plot()

print(f'\nSusceptible: {round(values[-1, 0], 2)}')
print(f'Infected ~ 0: {values[-1, 1] < 1}')
print(f'Recovered: {round(values[-1, 2], 2)}\n')