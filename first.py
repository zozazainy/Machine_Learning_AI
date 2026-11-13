print("Hello, Machine Learning!")
print("My Python learning journey starts.")
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Load your datasets
train_df = pd.read_csv('aug_train.csv')  # Assuming you have a training file
test_df = pd.read_csv('aug_test.csv')

# 2. Initialize the scaler
scaler = StandardScaler()

# 3. Fit and transform on training data, then ONLY transform on test data
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
