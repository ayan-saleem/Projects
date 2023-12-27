# Importing Packages
import pandas as pd                 # package for data processing
from termcolor import colored as cl # package for text customization
import numpy as np # package for working with arrays #Not being Used
import matplotlib.pyplot as plt # package for visualization #Not being Used

# Data being imported
df = pd.read_csv('creditcard.csv') # reads in the credit card dataset
df.drop('Time', axis=1, inplace=True) # drops the Time column

print(df.head()) # prints the first 5 rows of the modified dataset

# Counting of the dataset
cases = len(df) # counts the total number of cases
nonfraud_count = len(df[df.Class == 0]) # counts the number of non-fraud cases
fraud_count = len(df[df.Class == 1]) # counts the number of fraud cases
fraud_percentage = round(fraud_count / nonfraud_count * 100, 2) # calculates the percentage of fraud cases

# Makes a line
print(cl('--------------------------------------------', attrs=['bold'])) # prints another line of dashes

# Description of the dataset
nonfraud_cases = df[df.Class == 0] # creates a subset of non-fraud cases
fraud_cases = df[df.Class == 1] # creates a subset of fraud cases

# prints out the case amount statistics
print(cl('CASE AMOUNT STATISTICS', attrs=['bold'])) # prints "CASE AMOUNT STATISTICS" in bold
print(cl('--------------------------------------------', attrs=['bold'])) # prints a line of dashes
print(cl('NON-FRAUD CASE AMOUNT STATS', attrs=['bold'])) # prints "NON-FRAUD CASE AMOUNT STATS" in bold
print(nonfraud_cases.Amount.describe()) # prints the summary statistics of the amount column for non-fraud cases
print(cl('--------------------------------------------', attrs=['bold'])) # prints another line of dashes
print(cl('FRAUD CASE AMOUNT STATS', attrs=['bold'])) # prints "FRAUD CASE AMOUNT STATS" in bold
print(fraud_cases.Amount.describe()) # prints the summary statistics of the amount column for fraud cases
print(cl('--------------------------------------------', attrs=['bold'])) # prints another line of dashes

# prints out the case count statistics
print(cl('CASE COUNT', attrs=['bold'])) # prints "CASE COUNT" in bold
print(cl('--------------------------------------------', attrs=['bold'])) # prints a line of dashes
print(cl('Total number of cases are {}'.format(cases), attrs=['bold'])) # prints the total number of cases
print(cl('Number of Non-fraud cases are {}'.format(nonfraud_count), attrs=['bold'])) # prints the number of non-fraud cases
print(cl('Number of Fraud cases are {}'.format(fraud_count), attrs=['bold'])) # prints the number of fraud cases
print(cl('Percentage of fraud cases is {}'.format(fraud_percentage), attrs=['bold'])) # prints the percentage of fraud cases
print(cl('--------------------------------------------', attrs=['bold'])) # prints another line of dashes
