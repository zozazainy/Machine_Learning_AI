
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

print("Hello, Machine Learning!")
print("My Python learning journey starts.")

# Load dataset
df = pd.read_csv("aug_test.csv")

# Display dataset information
print("\nDataset:")
print(df.head())

print("\nDataset columns:")
print(df.columns)

# Select numerical columns
x = df.select_dtypes(include="number")

# Handle missing values
x = x.fillna(x.mean())

# Initialize scaler
scaler = StandardScaler()

# Scale numerical data
x_scaled = scaler.fit_transform(x)

print("\nOriginal data:")
print(x.head())

print("\nScaled data:")
print(x_scaled[:5])

print("\nMachine Learning preprocessing completed!")

# Logistic Regression
# This dataset has no target column, so training is not possible.

if "target" in df.columns:
    y = df["target"]

    model = LogisticRegression(max_iter=1000)
    model.fit(x_scaled, y)

    print("\nModel training completed!")
else:
    print("\nNo target column found!")
    print("Logistic Regression training cannot be performed.")

