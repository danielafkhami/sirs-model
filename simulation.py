import matplotlib.pyplot as plt
from params import *
from model import *

steps = int(T / dt)
valuesRK = np.zeros((steps, 3))
valuesE = np.zeros((steps, 3))
t_axis = np.linspace(0, T, steps)
valuesRK[0] = [S0, I0, R0]
valuesE[0] = [S0, I0, R0]

# Simulation
for i in range(1, steps):
    valuesRK[i] = RungeKutta(valuesRK[i-1], dt, sirs_system, beta, gamma, xi, N)
    valuesE[i] = RungeKutta(valuesE[i-1], dt, sirs_system, beta, gamma, xi, N)

def plot(values, method):
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t_axis, values[:, 0], label='Susceptible', color='blue')
    plt.plot(t_axis, values[:, 1], label='Infected', color='red')
    plt.plot(t_axis, values[:, 2], label='Recovered', color='green')

    plt.title(f"SIRS Model Simulation : {method}\n$\\beta={beta}, \\gamma={gamma}, \\xi={xi}$")
    plt.xlabel("Time (Days)")
    plt.ylabel("Population")
    plt.grid(alpha=0.3)
    plt.legend()

plot(valuesRK, "Runge-Kutta")
plot(valuesE, "Euler")
plt.show()

print(f'\nSusceptible RK: {round(valuesRK[-1, 0], 2)}')
print(f'Infected ~ 0 RK: {valuesRK[-1, 1] < 1}')
print(f'Recovered RK: {round(valuesRK[-1, 2], 2)}\n')
print(f'\nSusceptible E: {round(valuesE[-1, 0], 2)}')
print(f'Infected ~ 0 E: {valuesE[-1, 1] < 1}')
print(f'Recovered E: {round(valuesE[-1, 2], 2)}\n')