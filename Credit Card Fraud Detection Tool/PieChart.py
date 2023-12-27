# Importing packages
import pandas as pd
import matplotlib.pyplot as plt

# This reads the dataset
dataset = pd.read_csv("creditcard.csv")

# concatenate the first 5 and last 5 rows of the data
pd.concat([dataset.head(), dataset.tail()]) # This line does not store the data, so it will not show anything

# check for relative proportion
fraud_count = (dataset["Class"] == 1).sum()
valid_count = (dataset["Class"] == 0).sum()
total_count = dataset.shape[0]
print(f"Fraudulent Transactions: {fraud_count}") # This prints the fraudulent transactions
print(f"Real Transactions: {valid_count}") # This prints the number of real transactions
print(f"Proportion of Fraudulent Cases: {fraud_count / total_count:.4%}") # This prints the proportion of fraudulent cases.

# plot a pie chart to show the relative proportion of real and fraudulent transactions.
plt.pie([fraud_count, valid_count], labels=["Fraudulent Transactions", "Real Transactions"])
plt.show() # The pie chart will be displayed




