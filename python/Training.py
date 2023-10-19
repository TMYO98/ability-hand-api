import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import os

# Step 1: Data Preprocessing
folder_path = 'D:/Me/Trabajo 2023/Psyonic/ability-hand-api/python/DataForTraining/'  # Replace with your folder path
file_names = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
data = pd.concat([pd.read_csv(folder_path+file) for file in file_names])

# Calculate power in watts and take the absolute value
data['Power (W)'] = data['current'] * data['voltage']
data['Power (W)'] = data['Power (W)'].abs()

# Select relevant features
X = data[['Power (W)', 'temperature', 'Elapsed-Time']]
y = data['Motor-Temperature']
print(X)

# Step 4: Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Model Selection and Training
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R-squared (R2) Score: {r2}")

# Step 7: Predict Motor Temperature for new data
new_data = pd.DataFrame({'Power (W)': [new_power], 'temperature': [new_temperature], 'Elapsed-Time': [new_elapsed_time]})
predicted_motor_temperature = model.predict(new_data)

print(f"Predicted Motor Temperature: {predicted_motor_temperature[0]}")
