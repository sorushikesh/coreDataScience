# Population
# The entire group you want to study.
#
# - Denoted by: N (size), μ (mean), σ (std dev)
# - Example: All students in a country
#
# Sample
# A subset selected from the population for analysis.
#
# - Denoted by: n (size), x̄ (mean), s (std dev)
# - Example: 100 students from 5 universities


#
# Why Sampling?
# - Cost-effective
# - Time-saving
# - Often it's impossible to observe the whole population

# Key Differences
#
# | Feature            | Population                   | Sample                        |
# |--------------------|------------------------------|-------------------------------|
# | Size               | Usually large or infinite     | Small subset                  |
# | Notation (mean)    | μ                            | x̄                            |
# | Notation (std dev) | σ                            | s                             |
# | Measurement        | Parameter                    | Statistic                     |
# | Accuracy           | Exact (if measurable)         | Approximation                 |


import numpy as np
import pandas as pd

np.random.seed(42)
population = np.random.normal(loc=170, scale=10, size=10000)

# Sample of 100 people from the population
sample = np.random.choice(population, size=100, replace=False)

# Create a DataFrame
df = pd.DataFrame({
    'Population': population[:10],
    'Sample': np.append(sample[:10], [np.nan]*(10 - len(sample[:10])))
})

# Summary statistics
pop_mean = np.mean(population)
pop_std = np.std(population)
sample_mean = np.mean(sample)
sample_std = np.std(sample)

print(f"Population Mean (μ): {pop_mean:.2f}")
print(f"Population Std Dev (σ): {pop_std:.2f}")
print(f"Sample Mean (x̄): {sample_mean:.2f}")
print(f"Sample Std Dev (s): {sample_std:.2f}")

print()
print(df)
