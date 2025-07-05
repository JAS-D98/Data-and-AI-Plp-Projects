import pandas as pd    # data loading and manipulation
import numpy as np   # for numeric operations
from sklearn import linear_model   # linear regression and metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt   # for plots
from sklearn.model_selection import train_test_split


df=pd.read_csv("homeprices.csv")
print(df)

# visualize data
plt.figure(figsize=(8,6))
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($)')
plt.title('Scatter plot of Area vs Price')
plt.scatter( df.area, df.price, color='Red', marker='+' )
plt.grid(True)
plt.show()


# prepare data
X=df[['area']]
y=df['price']

# split dataset to training and test set
X_train,X_test,y_train,y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)

# Train Simple Linear Regression Model
reg=linear_model.LinearRegression()
reg.fit(X_train, y_train)

# model parameters
print("Coefficient (slope)", reg.coef_[0])
print("Intercept", reg.intercept_)


# Evaluate Model
y_pred = reg.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation Metrics (Simple Linear Regression):")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)

# Visualize Regression Line
plt.figure(figsize=(8,6))
plt.scatter(X, y, color='red', marker='+', label='Data Points')
plt.plot(X, reg.predict(X), color='blue', linewidth=2, label='Regression Line')
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($)')
plt.title('Regression Line Fit')
plt.legend()
plt.grid(True)
plt.show()


# Predict Price of 5000 sqft House
pred_price_5000 = reg.predict([[5000]])
print("\nPredicted price for 5000 sqft house:", pred_price_5000[0])

# Batch Predictions from areas.csv
area_df = pd.read_csv('areas.csv')
pred_prices = reg.predict(area_df)

# Combine areas and predictions
area_df['predicted_price'] = pred_prices
print(area_df)

# Save predictions to CSV
area_df.to_csv('predictions.csv', index=False)

# Multivariate Linear Regression
dfm = pd.read_csv('homeprices-m.csv')
print("\nMultivariate dataset:\n", dfm)

# Fill missing bedrooms with median
bedroom_median = dfm.bedrooms.median()
dfm.bedrooms = dfm.bedrooms.fillna(bedroom_median)

# Features and target
X_multi = dfm[['area', 'bedrooms', 'age']]
y_multi = dfm['price']

# Train multivariate regression model
mreg = linear_model.LinearRegression()
mreg.fit(X_multi, y_multi)

print("\nMultivariate Model Coefficients:", mreg.coef_)
print("Multivariate Model Intercept:", mreg.intercept_)

# Predict a specific case
# Example: 3000 sqft, 3 bedrooms, 40 years old
multi_pred = mreg.predict([[3000, 3, 40]])
print("Predicted price for 3000 sqft, 3 bedrooms, 40 years old:", multi_pred[0])
