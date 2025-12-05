import numpy as np
import scipy.stats as stats

# 1. Generate Mock Data (Since no data was provided)
# Assumptions: Drug lowers BP by ~15 points, Placebo by ~2 points (noise)
np.random.seed(42)
drug_group = np.random.normal(loc=15, scale=5, size=25)    # n=25
placebo_group = np.random.normal(loc=2, scale=5, size=25)  # n=25

def get_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    # sem = Standard Error of the Mean (std / sqrt(n))
    sem = stats.sem(data)
    
    # Calculate Interval using t-distribution
    # df = degrees of freedom (n-1)
    interval = stats.t.interval(confidence, df=n-1, loc=mean, scale=sem)
    return mean, interval

# 2. Calculate Intervals
drug_mean, drug_ci = get_confidence_interval(drug_group)
placebo_mean, placebo_ci = get_confidence_interval(placebo_group)

# 3. Output
print(f"--- Drug Group (n={len(drug_group)}) ---")
print(f"Mean Reduction: {drug_mean:.2f} mmHg")
print(f"95% Confidence Interval: {drug_ci[0]:.2f} to {drug_ci[1]:.2f} mmHg")

print(f"\n--- Placebo Group (n={len(placebo_group)}) ---")
print(f"Mean Reduction: {placebo_mean:.2f} mmHg")
print(f"95% Confidence Interval: {placebo_ci[0]:.2f} to {placebo_ci[1]:.2f} mmHg")