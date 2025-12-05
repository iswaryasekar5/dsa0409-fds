import numpy as np
from scipy import stats

# 1. Generate Mock Data (Daily conversion rates over 30 days)
# Design A: Mean 10%, Std Dev 2%
# Design B: Mean 12%, Std Dev 2.5%
np.random.seed(42)
design_a = np.random.normal(loc=0.10, scale=0.02, size=30)
design_b = np.random.normal(loc=0.12, scale=0.025, size=30)

# 2. Perform the Independent T-Test
# equal_var=False performs Welch's t-test, which is safer if variances differ
t_stat, p_value = stats.ttest_ind(design_a, design_b, equal_var=False)

# 3. Interpret Results
alpha = 0.05  # Standard significance level (95% confidence)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value:     {p_value:.4f}")
print("-" * 30)

if p_value < alpha:
    print("Result: Statistically SIGNIFICANT difference.")
    print("Reject the Null Hypothesis. Design B is performing differently.")
else:
    print("Result: NO statistically significant difference.")
    print("Fail to reject the Null Hypothesis. Differences are likely due to chance.")