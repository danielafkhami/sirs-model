N = 1000            # Total population
I0, R0 = 5, 0       # Initial infected and recovered
S0 = N - I0 - R0    # Initial susceptible
beta = 0.2          # Infectious rate
gamma = 0.1         # Recovery rate
xi = 0.005          # Immunity loss rate
lambd = 10.5        # birth rate
mu = 10             # death rate


T = 500             # Total time (days)
dt = 0.1            # Time step
