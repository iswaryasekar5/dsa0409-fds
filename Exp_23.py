import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
control = np.array([5.1, 5.3, 4.9, 5.0, 5.2, 5.1])
treatment = np.array([6.2, 6.5, 6.1, 6.3, 6.4, 6.6])
t_stat, p_value = stats.ttest_ind(treatment, control, equal_var=False)
print("T-Statistic:", round(t_stat, 4))
print("P-Value:", round(p_value, 6))
if p_value < 0.05:
    print("Result: Statistically significant effect.")
else:
    print("Result: No statistically significant effect.")
plt.figure(figsize=(8, 5))
plt.boxplot([control, treatment], labels=["Control", "Treatment"])
plt.title(f"Control vs Treatment\nP-Value = {p_value:.4f}")
plt.ylabel("Response Value")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()