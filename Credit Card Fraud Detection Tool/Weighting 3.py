# Pandas Framework
import pandas as pd

# Reads the CSV file
df = pd.read_csv("creditcard.csv")

# Select a subset of columns
df = df[["Time", "Amount", "Class"]]

# Calculates the weight of each data point
class_counts = df["Class"].value_counts()
weights = {0: 1 / class_counts[0], 1: 1 / class_counts[1]}
df["Weight"] = df["Class"].apply(lambda x: weights[x])

# Create a weighted sample
sample = df.sample(n=1000, weights="Weight", random_state=1)

# Print the sample
print(sample)
