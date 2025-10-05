import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    'budget': [100, 150, 200, 250, 300],
    'box_office': [110, 160, 210, 240, 310],
    'rating': [7.0, 7.5, 8.0, 7.8, 8.5]
}

df = pd.DataFrame(data)

corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

def correlation_strength(value):
    if abs(value) >= 0.9:
        return "Very Strong"
    elif abs(value) >= 0.7:
        return "Strong"
    elif abs(value) >= 0.5:
        return "Moderate"
    elif abs(value) >= 0.3:
        return "Weak"
    else:
        return "Very Weak"

labels = corr.copy().astype(str)
for i in range(corr.shape[0]):
    for j in range(corr.shape[1]):
        val = corr.iloc[i, j]
        if i == j:
            labels.iloc[i, j] = "X"  # diagonal
        else:
            labels.iloc[i, j] = f"{val:.2f}\n({correlation_strength(val)})"

plt.figure(figsize=(6, 4))
sns.heatmap(
    corr,
    mask=mask,
    annot=labels,
    fmt='',
    cmap="coolwarm",
    vmin=-1, vmax=1,
    square=True,
    linewidths=0.5
)
plt.title("Correlation Heatmap with Strength Labels (Diagonal Masked)")
plt.show()
