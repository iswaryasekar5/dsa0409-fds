import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Load the Data from the image
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)
print("--- Statistical Summary ---")
mean_vals = df.mean()
median_vals = df.median()
std_vals = df.std()

print(f"Mean:\n{mean_vals}\n")
print(f"Median:\n{median_vals}\n")
print(f"Standard Deviation:\n{std_vals}\n")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
df.boxplot(column=['age'])
plt.title('Boxplot of Age')
plt.ylabel('Years')

plt.subplot(1, 2, 2)
df.boxplot(column=['fat'])
plt.title('Boxplot of % Fat')
plt.ylabel('Percentage')

plt.suptitle('Distribution Analysis (Boxplots)')
plt.show()


# ---------------------------------------------------------
# Task 3: Draw Scatter Plot and Q-Q Plot
# ---------------------------------------------------------

# 3a. Scatter Plot (Age vs %Fat)
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['fat'], color='blue', alpha=0.7)
plt.title('Scatter Plot: Age vs. % Fat')
plt.xlabel('Age')
plt.ylabel('% Fat')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 3b. Q-Q Plots (Normality Check)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sm.qqplot(df['age'], line='s', ax=ax1)
ax1.set_title('Q-Q Plot: Age')

sm.qqplot(df['fat'], line='s', ax=ax2)
ax2.set_title('Q-Q Plot: % Fat')

plt.suptitle('Normality Check (Q-Q Plots)')
plt.show()