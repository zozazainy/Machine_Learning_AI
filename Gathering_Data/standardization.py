
import numpy as n
import pandas as p
import matplotlib.pyplot as t
import seaborn as s

df = p.read_csv("Social_Network_Ads.csv")

# print(df.sample(5))

# train test split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    df.drop('Purchased', axis=1),
    df['Purchased'],
    test_size=0.3,
    random_state=0
)

print(x_train.shape, x_test.shape)

# standard scaler
from sklearn.preprocessing import StandardScaler as ss

scaler = ss()
scaler.fit(x_train)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

# print(x_train_scaled)
# print(x_test_scaled)

print(scaler.mean_)

x_tr_scaled = p.DataFrame(x_train_scaled, columns=x_train.columns)
x_te_scaled = p.DataFrame(x_test_scaled, columns=x_test.columns)

# print(x_te_scaled)
# print(x_te_scaled)

print(n.round(x_train.describe(), 1))
print(n.round(x_tr_scaled.describe(), 1))

# effect of scaling

fig, (ax1, ax2) = t.subplots(ncols=2, figsize=(12, 5))

ax1.scatter(x_train['Age'], x_train['EstimatedSalary'])
ax1.set_title("Before Scaling")

ax2.scatter(
    x_tr_scaled['Age'],
    x_tr_scaled['EstimatedSalary'],
    color='red'
)
ax2.set_title("After Scaling")

t.show()

fig, (ax1, ax2) = t.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Before Scaling')
s.kdeplot(x_train['Age'], ax=ax1)
s.kdeplot(x_train['EstimatedSalary'], ax=ax1)

# after scaling
ax2.set_title('After Standard Scaling')
s.kdeplot(x_tr_scaled['Age'], ax=ax2)
s.kdeplot(x_tr_scaled['EstimatedSalary'], ax=ax2)

t.show()

# comparison of distribution

fig, (ax1, ax2) = t.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Age Distribution Before Scaling')
s.kdeplot(x_train['Age'], ax=ax1)

# after scaling
ax2.set_title('Age Distribution After Standard Scaling')
s.kdeplot(x_tr_scaled['Age'], ax=ax2)

t.show()

fig, (ax1, ax2) = t.subplots(ncols=2, figsize=(12, 5))

# before scaling
ax1.set_title('Salary Distribution Before Scaling')
s.kdeplot(x_train['EstimatedSalary'], ax=ax1)

# after scaling
ax2.set_title('Salary Distribution After Standard Scaling')
s.kdeplot(x_tr_scaled['EstimatedSalary'], ax=ax2)

t.show()

# why scaling is important

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr_scaled = LogisticRegression()

lr.fit(x_train, y_train)
lr_scaled.fit(x_train_scaled, y_train)

y_pred = lr.predict(x_test)
y_pred_scaled = lr_scaled.predict(x_test_scaled)

from sklearn.metrics import accuracy_score

print("actual", accuracy_score(y_test, y_pred))
print("scaled", accuracy_score(y_test, y_pred_scaled))

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt_scaled = DecisionTreeClassifier()

dt.fit(x_train, y_train)
dt_scaled.fit(x_train_scaled, y_train)

y_pred = dt.predict(x_test)
y_pred_scaled = dt_scaled.predict(x_test_scaled)

print("Actual", accuracy_score(y_test, y_pred))
print("Scaled", accuracy_score(y_test, y_pred_scaled))

print(df.describe())

# Add extreme outliers before the second split

outliers = p.DataFrame({
    'Age': [80, 90, 100],
    'EstimatedSalary': [200000, 250000, 300000],
    'Purchased': [0, 1, 1]
})

df = p.concat([df, outliers], ignore_index=True)

# visualize outliers

t.scatter(df['Age'], df['EstimatedSalary'])
t.title("Dataset with Outliers")
t.xlabel("Age")
t.ylabel("Estimated Salary")
t.show()

# train test split again

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df.drop('Purchased', axis=1),
    df['Purchased'],
    test_size=0.3,
    random_state=0
)

print(X_train.shape, X_test.shape)

# standard scaler

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# fit the scaler to the train set, it will learn the parameters
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = p.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = p.DataFrame(X_test_scaled, columns=X_test.columns)

# effect of scaling after adding outliers

fig, (ax1, ax2) = t.subplots(ncols=2, figsize=(12, 5))

ax1.scatter(X_train['Age'], X_train['EstimatedSalary'])
ax1.set_title("Before Scaling")

ax2.scatter(
    X_train_scaled['Age'],
    X_train_scaled['EstimatedSalary'],
    color='red'
)
ax2.set_title("After Scaling")

t.show()
