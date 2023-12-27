#Import required libraries
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

#Load data from creditcard.csv
data = pd.read_csv('creditcard.csv')

#Display the shape of the data
print(data.shape)

#Display summary statistics for each column
print(data.describe())

#Display the number of fraudulent and non-fraudulent transactions
print(data['Class'].value_counts())

#Separate features and labels
X = data.drop('Class', axis=1)
y = data['Class']

#Assign weights based on class labels (higher weight for fraudulent transactions)
weights = y.apply(lambda x: 2 if x == 1 else 1)

#Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Split the data into training and testing sets with 80/20 split
X_train, X_test, y_train, y_test, weights_train, weights_test = train_test_split(X, y, weights, test_size=0.2, random_state=42)

#Train a logistic regression model with class weight balanced
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train, sample_weight=weights_train)

#Predict labels for the test set
y_pred = model.predict(X_test)

#Print the performance metrics for the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1 Score:', f1_score(y_test, y_pred))
print('ROC AUC Score:', roc_auc_score(y_test, y_pred))

#Perform cross-validation with 5 folds and compute the mean score
scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')
print('Cross-Validation Scores:', scores)
print('Mean Score:', scores.mean())

#Create a new transaction with example features
new_transaction = [[-0.5, 1.2, 0.3, 0.2, -0.6, -0.2, 0.1, -0.3, 0.1, -0.5, 0.3, -0.1, -0.2, 0.1, -0.2, 0.2, 0.1, -0.1, 0.1, -0.3, 0.2, -0.2, -0.1, 0.1, -0.2, -0.3, 0.1, -0.2]]

#Scale the new transaction using the same scaler object used for the training set
new_transaction = scaler.transform(new_transaction)

#Predict whether the new transaction is fraudulent or not
print('Prediction:', model.predict(new_transaction))

#Normalise Data
#Load data from creditcard.csv
data = pd.read_csv('creditcard.csv')

#Separate features and labels
X = data.drop('Class', axis=1)
y = data['Class']

#Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Split the data into training and testing sets with 80/20 split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)