import numpy as np

# MPG of different car models
fuel_efficiency = np.array([22, 25, 28, 30, 34])

avg_mpg = np.mean(fuel_efficiency)

# Compare model index 1 and index 4
improvement = ((fuel_efficiency[4] - fuel_efficiency[1]) / fuel_efficiency[1]) * 100

print("Average MPG:", avg_mpg)
print("Improvement (%):", improvement)