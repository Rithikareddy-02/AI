# -*- coding: utf-8 -*-
"""AI Project Decision_Tree_me.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13TQidjQ4Sl3GNW5DFyXPCG7Mol7TNwiJ

Mount Drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""Import Libraries"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

"""Import Data"""

data = pd.read_csv("/content/drive/MyDrive/DATA_AI/AI_Project_data_final.csv")
data.head()

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

print(wt_min, cn_max, ip_max)

"""Missing Values Treatment"""

print(data.isnull().sum())

m_ip = data['IP'].mean()
m_psp = data['PSP'].mean()
m_elcs_lab = data['ELCS LAB'].mean()
m_eng1 = data['ENGLISH 1'].mean()
m_dbms = data['DBMS'].mean()
m_cn = data['CN'].mean()
m_wt = data['WT'].mean()

data['IP'].fillna(value = m_ip, inplace=True)
data['PSP'].fillna(value = m_psp, inplace=True)
data['ELCS LAB'].fillna(value = m_elcs_lab, inplace=True)
data['ENGLISH 1'].fillna(value = m_eng1, inplace=True)
data['DBMS'].fillna(value = m_dbms, inplace=True)
data['CN'].fillna(value = m_cn, inplace=True)
data['WT'].fillna(value = m_wt, inplace=True)

"""Normalisation"""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
# Applying scaler() to all the columns except the 'yes-no' and 'dummy' variables
num_vars = ['SSC', 'Inter', 'B.Tech 3-1', 'IP', 'PSP', 'ELCS LAB',
            'ENGLISH 1', 'DS', 'OS', 'DBMS', 'OOPC', 'CN', 'WT', 'Package']
data[num_vars] = scaler.fit_transform(data[num_vars])

data.head()

"""Data Split"""

from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(data, test_size = 0.05,random_state=1)

y_train = df_train.pop('Package')
X_train = df_train
y_test = df_test.pop('Package')
X_test = df_test

"""Model Training"""

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

"""Model Prediction"""

y_pred_train = regressor.predict(X_train)
df = pd.DataFrame({'Real Values':y_train, 'Predicted Values':y_pred_train})

y_pred_test = regressor.predict(X_test)
df1 = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_test})

"""Error Metrics"""

import math
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error

print('Training Errors')
# Traininig Accuracies
rmse = math.sqrt(mean_squared_error(y_train, y_pred_train)) 
print('Root mean square error', rmse) 
mse = (mean_squared_error(y_train, y_pred_train)) 
print('Mean square error', mse) 
mae = mean_absolute_error(y_train, y_pred_train)
print('Mean absolute error', mae)

import math
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error


#Testing Accuracies
rmse = math.sqrt(mean_squared_error(y_test, y_pred_test)) 
print('Root mean square error', rmse) 
mse = (mean_squared_error(y_test, y_pred_test)) 
print('Mean square error', mse) 
mae=mean_absolute_error(y_test, y_pred_test)
print('Mean absolute error', mae)

import matplotlib.pyplot as plt
import seaborn as sns
corr = data.corr()
plt.figure(figsize=(20,10))
sns.heatmap(corr, annot=True, cmap = 'coolwarm')

"""Save the Model"""

import pickle
# Save the model
filename = 'model.pkl'
pickle.dump(regressor, open(filename, 'wb'))

"""Deployment"""

list_of_columns = data.columns
input_data=pd.DataFrame(columns=list_of_columns)
input_data.drop(['Package'], axis='columns', inplace=True)


input_data.at[0, 'SSC'] = float(input('Enter SSC percentage'))
input_data.at[0, 'Inter'] = float(input('Enter Inter Percentage'))
input_data.at[0, 'B.Tech 3-1'] = float(input('Enter B.Tech 3-1 percentage'))
input_data.at[0, 'IP'] = int(input('enter marks in IP'))
input_data.at[0, 'PSP'] = int(input('enter marks in PSP'))
input_data.at[0, 'ELCS LAB'] = int(input('enter marks in ELCS LAB'))
input_data.at[0, 'ENGLISH 1'] = int(input('enter marks in ENGLISH 1'))
input_data.at[0, 'DS'] = int(input('enter marks in DS'))
input_data.at[0, 'OS'] = int(input('enter marks in OS'))
input_data.at[0, 'DBMS'] = int(input('enter marks in DBMS'))
input_data.at[0, 'OOPC'] = int(input('enter marks in OOPC'))
input_data.at[0, 'CN'] = int(input('enter marks in CN'))
input_data.at[0, 'WT'] = int(input('enter marks in WT'))

# De-normalisation
input_data['SSC']=(input_data['SSC']-ssc_min)/(ssc_max-ssc_min)
input_data['Inter']=(input_data['Inter']-inter_min)/(inter_max-inter_min)
input_data['B.Tech 3-1']=(input_data['B.Tech 3-1']-btech_min)/(btech_max-btech_min)
input_data['IP']=(input_data['IP']-ip_min)/(ip_max-ip_min)
input_data['PSP']=(input_data['PSP']-psp_min)/(psp_max-psp_min)
input_data['ELCS LAB']=(input_data['ELCS LAB']-elcs_min)/(elcs_max-elcs_min)
input_data['ENGLISH 1']=(input_data['ENGLISH 1']-eng1_min)/(eng1_max-eng1_min)
input_data['DS']=(input_data['DS']-ds_min)/(ds_max-ds_min)
input_data['OS']=(input_data['OS']-os_min)/(os_max-os_min)
input_data['DBMS']=(input_data['DBMS']-dbms_min)/(dbms_max-dbms_min)
input_data['OOPC']=(input_data['OOPC']-oopc_min)/(oopc_max-oopc_min)
input_data['CN']=(input_data['CN']-cn_min)/(cn_max-cn_min)
input_data['WT']=(input_data['WT']-wt_min)/(wt_max-wt_min)

result = regressor.predict(input_data)
package=result*(package_max-package_min)+package_min
print('Package = ', package)