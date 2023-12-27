import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('creditcard.csv')

# Split the DataFrame into X and y
X = df.drop('Class', axis=1)
y = df['Class']

# Normalize the feature matrix X
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Optionally, visualize the normalized data
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].hist(X[:, 0], bins=50)
axs[0].set_xlabel('Feature 1')
axs[0].set_ylabel('Count')
axs[1].hist(X[:, 1], bins=50)
axs[1].set_xlabel('Feature 2')
axs[1].set_ylabel('Count')
plt.show()
