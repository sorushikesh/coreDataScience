# Rank Transformation and Tied Ranks
#
# In statistics and machine learning, rank transformation is the process of replacing data values
# with their ranks when sorted.
# This technique is commonly used in non-parametric statistical tests like Spearman correlation.

# When multiple values are the same, we call them ties. These tied values can be ranked in different ways,
# depending on the method used.


# Ranking Methods in Python (`scipy.stats.rankdata`)
#
# - average: Assigns the average rank to each tied group.
# - min: Assigns the minimum rank to tied values.
# - max: Assigns the maximum rank to tied values.
# - dense: Like `min`, but ranks increment by 1 without gaps.
# - ordinal: Each value gets a unique rank (no tie handling).

import pandas as pd
from scipy.stats import rankdata

data = [50, 20, 30, 20, 90, 30]
df = pd.DataFrame({'Value': data})

# Apply different ranking methods
df['Rank (average)'] = rankdata(df['Value'], method='average')
df['Rank (min)'] = rankdata(df['Value'], method='min')
df['Rank (max)'] = rankdata(df['Value'], method='max')
df['Rank (dense)'] = rankdata(df['Value'], method='dense')
df['Rank (ordinal)'] = rankdata(df['Value'], method='ordinal')

print()
print(df)
print()

# When is Rank Transformation Useful?
#
# - When data does not follow a normal distribution.
# - When using non-parametric methods like:
#   - Spearman correlation
#   - Wilcoxon signed-rank test
#   - Kruskal-Wallis H-test
# - To reduce the impact of outliers.
#
# Rank transformation is also a common preprocessing step before applying certain types of machine learning
# models.


