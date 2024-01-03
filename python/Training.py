import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import os
import matplotlib.pyplot as plt

integral_len = 40
integral_len2 = 80
Kt = 0.000
integral = 0

# Step 1: Data Preprocessing
# folder_path = 'C:/Users/jctam/OneDrive/Escritorio/PSYONIC/ability-hand-api/python/DataForTraining/'  # Replace with your folder path
# file_names = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
# data = pd.concat([pd.read_csv(folder_path+file) for file in file_names])
data = pd.read_csv('C:/Users/jctam/OneDrive/Escritorio/PSYONIC/ability-hand-api/python/DataForTraining/AI_Data_TestOTHERtemp2.csv')

# Calculate power in watts and take the absolute value
data['Power (W)'] = data['current'] * data['voltage']
data['Power (W)'] = data['Power (W)'].abs()
data['Power_Integ'] = data['Power (W)'].abs()
data['Temp_Observer'] = data['Motor-Temperature']
lenght = len(data['Power (W)'])
cooling_Ratio = 0
# print(data['Temp_Observer'])


Power = [0] * integral_len #Init empty array
Power2 = [0] * integral_len2 #Init empty array
for j in range (lenght):
    for i in range(integral_len-1,0,-1):
        Power[i] = Power[i-1] 
    for i in range(integral_len2-1,0,-1):
        Power2[i] = Power2[i-1]       
    Power[0] = data['Power (W)'][j]
    Power2[0] = data['Power (W)'][j]
    data['Power_Integ'][j] = sum(Power)*.00016
    integral = sum(Power2)*.000003
    if(j>1):
        if(integral == 0 and data['Temp_Observer'][j-1] >25):
            cooling_Ratio = -0.000009 * data['Temp_Observer'][j-1]
        else:
            cooling_Ratio = integral
        data['Temp_Observer'][j] = data['Power_Integ'][j] + cooling_Ratio + data['Temp_Observer'][j-1]


# Select relevant features
# X = data[['Power (W)', 'temperature', 'Elapsed-Time']]
X = data[['Power (W)', 'temperature','Motor-Temperature']]
y = data['Elapsed-Time']

# print(X)
# print(y)

plt.plot(data[['Power (W)']], label= "Power")
plt.plot(data[['temperature']], label= "uTemp")
plt.plot(data[['Motor-Temperature']], label= "mTemp")
plt.plot(data[['Power_Integ']], label= "Pow_int")
plt.plot(data[['Temp_Observer']], label= "Temp_obs")
plt.legend()
plt.show()

# # Step 4: Split the Data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Step 5: Model Selection and Training
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Step 6: Model Evaluation
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y_test, y_pred)

# print(f"Mean Squared Error: {mse}")
# print(f"Root Mean Squared Error: {rmse}")
# print(f"R-squared (R2) Score: {r2}")

# # Step 7: Predict Motor Temperature for new data
# new_data = pd.DataFrame({'Power (W)': [new_power], 'temperature': [new_temperature], 'Elapsed-Time': [new_elapsed_time]})
# predicted_motor_temperature = model.predict(new_data)

# print(f"Predicted Motor Temperature: {predicted_motor_temperature[0]}")
