import numpy as np
from scipy import optimize

# Define the function you want to minimize
def f(n):
    #return n*
    return 0

# Use optimize.minimize, providing an initial guess (x0)
# This finds a local minimum
result = optimize.minimize(f, x0=0)

print(f"Minimum function value (fun): {result.fun}")
print(f"Optimal x value (x): {result.x}")