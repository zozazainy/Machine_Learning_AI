import pandas as pd
from sklearn.preprocessing import StandardScaler

print("Hello, Machine Learning!")
print("My Python learning journey starts.")

# Load the available dataset
df = pd.read_csv("aug_test.csv")

# Select numerical columns
x = df.select_dtypes(include="number")

# Handle missing values
x = x.fillna(x.mean())

# Initialize scaler
scaler = StandardScaler()

# Scale the data
x_scaled = scaler.fit_transform(x)

print("Original data:")
print(x.head())

print("Scaled data:")
print(x_scaled[:5])

print("Machine Learning preprocessing completed!")