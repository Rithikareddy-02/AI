"""Import Libraries"""

# importing libraries  
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd

"""Load Data"""

excel_file = 'AI_Project_Data_1.xlsx'
sheet_name = 'data'

data  = pd.read_excel(excel_file,
                    sheet_name = sheet_name,
                    usecols = 'A:N',
                    header = 0)

"""Missing Values Treatment"""

data.isnull().sum()

m_ip = data['IP'].mean()
m_psp = data['PSP'].mean()
m_elcslab = data['ELCS LAB'].mean()
m_eng1 = data['ENGLISH 1'].mean()
m_dbms = data['DBMS'].mean()
m_cn  = data['CN'].mean()
m_wt = data['WT'].mean()

data['IP'].fillna(value = m_ip, inplace=True) 
data['PSP'].fillna(value = m_psp, inplace=True)
data['ELCS LAB'].fillna(value = m_elcslab, inplace=True)
data['ENGLISH 1'].fillna(value = m_eng1, inplace=True)
data['DBMS'].fillna(value = m_dbms, inplace=True)
data['CN'].fillna(value = m_cn, inplace=True)
data['WT'].fillna(value = m_wt, inplace=True)

"""Min and Max Values"""

ssc_min = data['SSC'].min()
ssc_max = data['SSC'].max()
inter_min = data['Inter'].min()
inter_max = data['Inter'].max()
btech_min = data['B.Tech 3-1'].min()
btech_max = data['B.Tech 3-1'].max()
ip_min = data['IP'].min()
ip_max = data['IP'].max()
psp_min = data['PSP'].min()
psp_max = data['PSP'].max()
elcs_min = data['ELCS LAB'].min()
elcs_max = data['ELCS LAB'].max()
eng1_min = data['ENGLISH 1'].min()
eng1_max = data['ENGLISH 1'].max()
ds_min = data['DS'].min()
ds_max = data['DS'].max()
os_min = data['OS'].min()
os_max = data['OS'].max()
dbms_min = data['DBMS'].min()
dbms_max = data['DBMS'].max()
oopc_min = data['OOPC'].min()
oopc_max = data['OOPC'].max()
cn_min = data['CN'].min()
cn_max = data['CN'].max()
wt_min = data['WT'].min()
wt_max = data['WT'].max()
package_min = data['Package'].min()
package_max = data['Package'].max()

"""Normalisation"""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
# Applying scaler() to all the columns except the 'yes-no' and 'dummy' variables
num_vars = ['SSC', 'Inter', 'B.Tech 3-1', 'IP', 'PSP', 'ELCS LAB',
            'ENGLISH 1', 'DS', 'OS', 'DBMS', 'OOPC', 'CN', 'WT', 'Package']
data[num_vars] = scaler.fit_transform(data[num_vars])


"""Data Split"""

from sklearn.model_selection import train_test_split
feature_cols = ['SSC', 'Inter', 'B.Tech 3-1', 'IP', 'PSP', 'ELCS LAB',
                'ENGLISH 1', 'DS', 'OS', 'DBMS', 'OOPC', 'CN', 'WT']
X = data[feature_cols] 
y = data.Package
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state = 1)

"""Model Training"""

#Fitting Decision Tree classifier to the training set  
from sklearn.ensemble import RandomForestRegressor
regressor= RandomForestRegressor(n_estimators= 3)  
regressor.fit(X_train, y_train)

"""Model Prediction"""

#Predicting the test set result  
y_pred= regressor.predict(X_test)

"""Error Metrics"""

import math
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error


#Testing Accuracies
rmse = math.sqrt(mean_squared_error(y_test, y_pred)) 
print('Root mean square error', rmse) 
mse = (mean_squared_error(y_test, y_pred)) 
print('Mean square error', mse) 
mae=mean_absolute_error(y_test, y_pred)
print('Mean absolute error', mae)