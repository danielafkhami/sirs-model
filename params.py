N = 1000            # Total population
I0, R0 = 1, 0       # Initial infected and recovered
S0 = N - I0 - R0    # Initial susceptible
beta = 0.3          # Infectious rate
gamma = 0.1         # Recovery rate
xi = 0.05           # Immunity loss rate
birth = 10          # birth rate
death = 12          # death rate

T = 500             # Total time (days)
dt = 0.1            # Time step