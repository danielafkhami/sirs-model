N = 1000            # Total population
I0, R0 = 1, 0       # Initial infected and recovered
S0 = N - I0 - R0    # Initial susceptible
beta = 0.6          # Infectious rate
gamma = 0.1         # Recovery rate
xi = 0.04           # Immunity loss rate

T = 200             # Total time (days)
dt = 0.1            # Time step